import subprocess
import re
import argparse
import sys
import shlex
import requests
import os

# 🔐 Default Slack user IDs to mention in alert (override via --slack-user-ids)
DEFAULT_SLACK_USER_IDS = ["UED14KCLE", "U088B1A3ZN2"]

def get_battery_info():
    try:
        battery_path_cmd = "upower -e | grep 'BAT'"
        battery_path = subprocess.check_output(battery_path_cmd, shell=True).decode().strip()

        battery_info_cmd = f"upower -i {battery_path}"
        output = subprocess.check_output(battery_info_cmd, shell=True).decode()

        return output
    except subprocess.CalledProcessError as e:
        print("Error getting battery info:", e)
        sys.exit(1)

def parse_battery_info(info):
    battery_state = {}
    for line in info.splitlines():
        line = line.strip()
        if line.startswith("state:"):
            battery_state["state"] = line.split(":", 1)[1].strip().lower()
        elif line.startswith("percentage:"):
            battery_state["percentage"] = int(re.findall(r'\d+', line)[0])
    return battery_state

def send_slack_alert(webhook_url, percentage, state, reason, slack_user_ids):
    if not webhook_url:
        return
    user_mentions = " ".join(f"<@{uid}>" for uid in slack_user_ids)

    message = (
        f":warning: {user_mentions} Battery is at {percentage}% and is *{state}*. {reason} :electric_plug:"
    )
    payload = {"text": message}

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code != 200:
            print(f"Slack webhook failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Slack alert error: {e}")

def get_logged_in_graphical_users():
    """Return list of {user, uid, display} for active graphical sessions."""
    users = []
    try:
        out = subprocess.check_output(["who"], stderr=subprocess.DEVNULL).decode()
    except Exception:
        return users
    seen = set()
    for line in out.splitlines():
        parts = line.split()
        if not parts:
            continue
        display = None
        for token in parts:
            m = re.match(r"^\(?(:\d+(\.\d+)?)\)?$", token)
            if m:
                display = m.group(1)
                break
        if not display:
            continue
        username = parts[0]
        key = (username, display)
        if key in seen:
            continue
        seen.add(key)
        try:
            uid = int(subprocess.check_output(["id", "-u", username]).decode().strip())
        except Exception:
            continue
        users.append({"user": username, "uid": uid, "display": display})
    return users

def send_desktop_alert(title, message, urgency="critical"):
    """Send a desktop notification to every logged-in graphical user, plus wall fallback."""
    sessions = get_logged_in_graphical_users()
    running_as_root = (os.geteuid() == 0) if hasattr(os, "geteuid") else False

    if not sessions:
        try:
            subprocess.run(["notify-send", "-u", urgency, title, message], check=False)
        except FileNotFoundError:
            pass
    else:
        for s in sessions:
            env_prefix = (
                f"DISPLAY={s['display']} "
                f"DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/{s['uid']}/bus "
                f"XDG_RUNTIME_DIR=/run/user/{s['uid']}"
            )
            notify_cmd = (
                f"{env_prefix} notify-send -u {urgency} "
                f"{shlex.quote(title)} {shlex.quote(message)}"
            )
            if running_as_root:
                cmd = f"sudo -u {shlex.quote(s['user'])} bash -c {shlex.quote(notify_cmd)}"
            else:
                cmd = notify_cmd
            subprocess.run(cmd, shell=True, check=False)

    try:
        subprocess.run(["wall", f"{title}: {message}"], check=False)
    except FileNotFoundError:
        pass

def send_whatsapp_alert(phone, apikey, message):
    """Send a WhatsApp alert using the CallMeBot API. Never raises; failures are logged only."""
    try:
        if not phone or not apikey:
            return
        url = "https://api.callmebot.com/whatsapp.php"
        params = {"phone": phone, "text": message, "apikey": apikey}
        try:
            resp = requests.get(url, params=params, timeout=15)
        except requests.RequestException as e:
            print(f"WhatsApp alert network error: {e}")
            return
        if resp.status_code != 200:
            print(f"WhatsApp alert failed: HTTP {resp.status_code}, {resp.text[:200]}")
    except Exception as e:
        print(f"WhatsApp alert unexpected error: {e}")

def initiate_shutdown(delay_minutes, message):
    """Schedule a system shutdown with a warning message broadcast to logged-in users."""
    try:
        subprocess.run(
            ["shutdown", "-h", f"+{delay_minutes}", message],
            check=False,
        )
    except FileNotFoundError:
        print("`shutdown` command not found; cannot initiate shutdown.")

def dispatch_alerts(percentage, state, reason, urgency, cfg):
    """Send the alert to all enabled channels."""
    title = f"Battery Alert ({percentage}%)"
    body = f"Battery is at {percentage}% and is {state}. {reason}"

    if cfg["enable_desktop_alert"]:
        send_desktop_alert(title, body, urgency=urgency)

    send_slack_alert(cfg["webhook_url"], percentage, state, reason, cfg["slack_user_ids"])

    if cfg["enable_whatsapp"]:
        try:
            send_whatsapp_alert(cfg["whatsapp_phone"], cfg["whatsapp_apikey"], body)
        except Exception as e:
            # Belt-and-suspenders: WhatsApp failures must never break the alert flow.
            print(f"WhatsApp alert dispatch suppressed: {e}")

def main(cfg):
    info = get_battery_info()
    battery = parse_battery_info(info)

    percentage = battery.get("percentage")
    state = battery.get("state")

    if percentage is None or state is None:
        print("Could not parse battery percentage or state.")
        sys.exit(1)

    if cfg["force_alert"]:
        reason = f"Forced alert: Battery is at {percentage}% and state is '{state}'."
        dispatch_alerts(percentage, state, reason, "critical", cfg)
        return

    if state != "charging" and percentage <= cfg["shutdown_threshold"]:
        reason = (
            f"Battery critically low ({percentage}% <= {cfg['shutdown_threshold']}%). "
            f"Shutting down in {cfg['shutdown_delay_minutes']} minute(s)."
        )
        dispatch_alerts(percentage, state, reason, "critical", cfg)
        if cfg["enable_shutdown"]:
            initiate_shutdown(
                cfg["shutdown_delay_minutes"],
                f"Battery at {percentage}% - shutting down to protect data.",
            )
        else:
            print("Shutdown not enabled (pass --enable-shutdown to activate); alert only.")
        return

    if state != "charging" and percentage < cfg["lower_threshold"]:
        reason = f"Battery is low (below {cfg['lower_threshold']}%) and not charging. Please plug in."
        dispatch_alerts(percentage, state, reason, "critical", cfg)

    elif state == "charging" and percentage > cfg["upper_threshold"]:
        reason = f"Battery is high (above {cfg['upper_threshold']}%) and still charging. Consider unplugging."
        dispatch_alerts(percentage, state, reason, "normal", cfg)

    else:
        print(f"Battery is at {percentage}% and state is '{state}'. No alert needed.")

def _safe_int(value, fallback):
    """Parse an int safely; return fallback on any error so cron never crashes on bad env vars."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback

def _env_flag(name, default=False):
    """Read a boolean from env: 1/true/yes/on (case-insensitive) -> True; else default."""
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")

def build_config_from_args(args):
    webhook_url = args.slack_webhook_url or os.getenv("SLACK_PERSONAL_ALERTS_WEBHOOK_URL", "")

    if args.slack_user_ids:
        slack_user_ids = [uid.strip() for uid in args.slack_user_ids.split(",") if uid.strip()]
    else:
        env_ids = os.getenv("SLACK_USER_IDS", "")
        slack_user_ids = [uid.strip() for uid in env_ids.split(",") if uid.strip()] or DEFAULT_SLACK_USER_IDS

    whatsapp_phone = args.whatsapp_phone or os.getenv("WHATSAPP_PHONE", "")
    whatsapp_apikey = args.whatsapp_apikey or os.getenv("WHATSAPP_APIKEY", "")
    enable_whatsapp = (args.enable_whatsapp or _env_flag("BATTERY_ENABLE_WHATSAPP")) \
        and bool(whatsapp_phone) and bool(whatsapp_apikey)

    enable_shutdown = args.enable_shutdown or _env_flag("BATTERY_ENABLE_SHUTDOWN")
    enable_desktop_alert = args.enable_desktop_alert or _env_flag("BATTERY_ENABLE_DESKTOP_ALERT")

    return {
        "lower_threshold": args.lower_threshold,
        "upper_threshold": args.upper_threshold,
        "shutdown_threshold": args.shutdown_threshold,
        "shutdown_delay_minutes": args.shutdown_delay_minutes,
        "enable_shutdown": enable_shutdown,
        "enable_desktop_alert": enable_desktop_alert,
        "enable_whatsapp": enable_whatsapp,
        "force_alert": args.force_alert,
        "webhook_url": webhook_url,
        "slack_user_ids": slack_user_ids,
        "whatsapp_phone": whatsapp_phone,
        "whatsapp_apikey": whatsapp_apikey,
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Laptop battery monitor with multi-channel alerts.")
    parser.add_argument("--lower-threshold", type=int,
                        default=_safe_int(os.getenv("BATTERY_LOWER_THRESHOLD"), 35),
                        help="Lower battery threshold percentage (default: 35)")
    parser.add_argument("--upper-threshold", type=int,
                        default=_safe_int(os.getenv("BATTERY_UPPER_THRESHOLD"), 80),
                        help="Upper battery threshold percentage (default: 80)")
    parser.add_argument("--shutdown-threshold", type=int,
                        default=_safe_int(os.getenv("BATTERY_SHUTDOWN_THRESHOLD"), 15),
                        help="Battery percentage at or below which the system will shut down if --enable-shutdown is set (default: 15)")
    parser.add_argument("--shutdown-delay-minutes", type=int,
                        default=_safe_int(os.getenv("BATTERY_SHUTDOWN_DELAY_MIN"), 1),
                        help="Minutes to wait before shutting down (default: 1)")
    parser.add_argument("--enable-shutdown", action="store_true",
                        help="Opt in to actually shut down when battery <= --shutdown-threshold (off by default)")
    parser.add_argument("--enable-desktop-alert", action="store_true",
                        help="Opt in to send desktop notifications (notify-send) to all logged-in graphical users (off by default)")
    parser.add_argument("--slack-webhook-url", type=str, default="",
                        help="Slack webhook URL (falls back to SLACK_PERSONAL_ALERTS_WEBHOOK_URL env var)")
    parser.add_argument("--slack-user-ids", type=str, default="",
                        help="Comma-separated Slack user IDs to mention (falls back to SLACK_USER_IDS env var)")
    parser.add_argument("--enable-whatsapp", action="store_true",
                        help="Opt in to send WhatsApp alerts via CallMeBot (requires --whatsapp-phone and --whatsapp-apikey)")
    parser.add_argument("--whatsapp-phone", type=str, default="",
                        help="WhatsApp phone number with country code, e.g. +911234567890 (or WHATSAPP_PHONE env var)")
    parser.add_argument("--whatsapp-apikey", type=str, default="",
                        help="CallMeBot WhatsApp API key (or WHATSAPP_APIKEY env var)")
    parser.add_argument("--force-alert", "--force-slack-alert", dest="force_alert", action="store_true",
                        help="Force alert on all enabled channels irrespective of battery state")

    args = parser.parse_args()
    main(build_config_from_args(args))

# Examples:
#
# 1) Existing/legacy cron (Slack-only) — keeps working unchanged, no new features activated:
# */5 * * * * /usr/bin/python3 /study-zone/GitHub/Python-BootCamp/miscellaneous/laptop_battery_alert.py \
#     --slack-webhook-url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
#
# 2) Opt in to desktop notifications + auto-shutdown at <=15% (run as root so shutdown / notify-send to other users work):
# sudo crontab -e
# */5 * * * * /usr/bin/python3 /study-zone/GitHub/Python-BootCamp/miscellaneous/laptop_battery_alert.py \
#     --slack-webhook-url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX" \
#     --enable-desktop-alert --enable-shutdown
#
# 3) Add WhatsApp alerts via CallMeBot:
# */5 * * * * /usr/bin/python3 /study-zone/GitHub/Python-BootCamp/miscellaneous/laptop_battery_alert.py \
#     --slack-webhook-url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX" \
#     --enable-desktop-alert --enable-shutdown \
#     --enable-whatsapp --whatsapp-phone="+911234567890" --whatsapp-apikey="123456"
#
# 4) Force a test alert on all enabled channels:
# python3 miscellaneous/laptop_battery_alert.py --force-alert \
#     --slack-webhook-url="https://hooks.slack.com/services/..." \
#     --enable-desktop-alert --enable-whatsapp --whatsapp-phone="+91..." --whatsapp-apikey="..."

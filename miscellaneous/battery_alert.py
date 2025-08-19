import subprocess
import re
import argparse
import sys
import requests
import os

# 🔐 Hardcoded Slack user IDs to mention in alert
SLACK_USER_IDS = ["UED14KCLE", "U088B1A3ZN2"]  # Replace with actual user IDs

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

def send_slack_alert(webhook_url, percentage, state, reason):
    user_mentions = " ".join(f"<@{uid}>" for uid in SLACK_USER_IDS)

    message = (
        f":warning: {user_mentions} Battery is at {percentage}% and is *{state}*. {reason} :electric_plug:"
    )
    payload = {"text": message}

    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Slack webhook failed: {response.status_code}, {response.text}")

def main(lower_threshold, upper_threshold, force_slack_alert, slack_webhook_url):
    if slack_webhook_url == "":
        webhook_url = os.getenv("SLACK_PERSONAL_ALERTS_WEBHOOK_URL")
    else:
        webhook_url = slack_webhook_url

    if not webhook_url:
        print("Environment variable SLACK_PERSONAL_ALERTS_WEBHOOK_URL is not set.")
        sys.exit(1)

    info = get_battery_info()
    battery = parse_battery_info(info)

    percentage = battery.get("percentage")
    state = battery.get("state")

    if percentage is None or state is None:
        print("Could not parse battery percentage or state.")
        sys.exit(1)

    if force_slack_alert:
        reason = f"Forced alert: Battery is at {percentage}% and state is '{state}'."
        send_slack_alert(webhook_url, percentage, state, reason)
        return

    if state != "charging" and percentage < lower_threshold:
        reason = f"Battery is low (below {lower_threshold}%) and not charging. Please plug in."
        send_slack_alert(webhook_url, percentage, state, reason)

    elif state == "charging" and percentage > upper_threshold:
        reason = f"Battery is high (above {upper_threshold}%) and still charging. Consider unplugging."
        send_slack_alert(webhook_url, percentage, state, reason)

    else:
        print(f"Battery is at {percentage}% and state is '{state}'. No alert needed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lower-threshold", type=int, default=35, help="Lower battery threshold percentage")
    parser.add_argument("--upper-threshold", type=int, default=80, help="Upper battery threshold percentage")
    parser.add_argument("--slack-webhook-url", type=str, default="", help="Slack webhook URL for alerts")
    parser.add_argument("--force-slack-alert", action="store_true", help="Force Slack alert irrespective of battery state")

    args = parser.parse_args()
    main(args.lower_threshold, args.upper_threshold, args.force_slack_alert, args.slack_webhook_url)

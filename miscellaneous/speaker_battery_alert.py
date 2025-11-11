import subprocess
import re
import argparse
import sys
import requests
import os
import json

# 🔐 Hardcoded Slack user IDs to mention in alert
SLACK_USER_IDS = ["UED14KCLE", "U088B1A3ZN2"]  # Replace with actual user IDs

def get_upower_devices():
    """Return list of all UPower device paths."""
    result = subprocess.run(["upower", "-e"], capture_output=True, text=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

def get_device_info(device_path):
    """Return 'upower -i' output as dict."""
    result = subprocess.run(["upower", "-i", device_path], capture_output=True, text=True)
    info = {}
    for line in result.stdout.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            info[key.strip()] = val.strip()
    return info

def find_device_by_model(device_name):
    """Return UPower device path that matches the given model name."""
    for path in get_upower_devices():
        info = get_device_info(path)
        if info.get("model", "").lower() == device_name.lower():
            return path, info
    return None, None

def send_slack_alert(webhook_url, percentage, state, reason):
    user_mentions = " ".join(f"<@{uid}>" for uid in SLACK_USER_IDS)

    message = (
        f":warning: {user_mentions} Battery is at {percentage}% and is *{state}*. {reason} :electric_plug:"
    )
    payload = {"text": message}

    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Slack webhook failed: {response.status_code}, {response.text}")

def main(device_name, lower_threshold, upper_threshold, force_slack_alert, slack_webhook_url):
    if slack_webhook_url == "":
        webhook_url = os.getenv("SLACK_PERSONAL_ALERTS_WEBHOOK_URL")
    else:
        webhook_url = slack_webhook_url

    if not webhook_url:
        print("Environment variable SLACK_PERSONAL_ALERTS_WEBHOOK_URL is not set.")
        sys.exit(1)

    path, info = find_device_by_model(device_name)

    if not path:
        print(f"❌ Device '{device_name}' not found via UPower.")
        sys.exit(1)

    percentage = info.get("percentage", "Unknown").strip('%')
    message = f"🔋 *{device_name}* battery level: {percentage}%"
    print(message)

    # state = battery.get("state")

    # if percentage is None or state is None:
    #     print("Could not parse battery percentage or state.")
    #     sys.exit(1)

    # if force_slack_alert:
    #     reason = f"Forced alert: Battery is at {percentage}% and state is '{state}'."
    #     send_slack_alert(webhook_url, percentage, state, reason)
    #     return

    # if state != "charging" and percentage < lower_threshold:
    #     reason = f"Battery is low (below {lower_threshold}%) and not charging. Please plug in."
    #     send_slack_alert(webhook_url, percentage, state, reason)

    # elif state == "charging" and percentage > upper_threshold:
    #     reason = f"Battery is high (above {upper_threshold}%) and still charging. Consider unplugging."
    #     send_slack_alert(webhook_url, percentage, state, reason)

    # else:
    #     print(f"Battery is at {percentage}% and state is '{state}'. No alert needed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lower_threshold", type=int, default=35, help="Lower battery threshold percentage")
    parser.add_argument("--upper_threshold", type=int, default=80, help="Upper battery threshold percentage")
    parser.add_argument("--slack_webhook_url", type=str, default="", help="Slack webhook URL for alerts")
    parser.add_argument("--device_name", type=str, default="", help="Slack webhook URL for alerts")
    parser.add_argument("--force_slack_alert", action="store_true", help="Force Slack alert irrespective of battery state")

    args = parser.parse_args()
    main(args.device_name, args.lower_threshold, args.upper_threshold, args.force_slack_alert, args.slack_webhook_url)

# python speaker_battery_alert.py --device_name "Aavante Bar Aspire" --slack_webhook_url "$SLACK_WEBHOOK_URL"



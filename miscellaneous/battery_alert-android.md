# Battery Alert for Android Mobile

## [Using Termux + Python script](https://f-droid.org/packages/com.termux/)
  - [Remote Access](https://wiki.termux.dev/wiki/Remote_Access)
```
pkg install openssh -y
passwd
sshd
ssh -p 8022 u0_a$(id -u)@saanvi-mobile


# Check battery
termux-battery-status

# Schedule with termux-job-scheduler or Android’s Termux:API add-on.

pkg install python termux-api -y
pip install requests
pkg install nodejs -y
npm install -g termux-web
termux-web
python -m http.server 8080



nano battery_slack_alert.py

python battery_slack_alert.py

termux-job-scheduler --script ~/battery_slack_alert.py --period-ms 3600000



```

## battery_slack_alert.py

```
import subprocess
import json
import requests

# --- CONFIG ---
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"  # ← replace with your webhook
THRESHOLD = 35  # alert if battery % is below this value
DEVICE_NAME = "Ajay’s Phone"  # change as you like

def get_battery_level():
    """Get battery info from Termux API"""
    try:
        result = subprocess.check_output(["termux-battery-status"])
        data = json.loads(result)
        return data.get("percentage", None)
    except Exception as e:
        print(f"Error reading battery level: {e}")
        return None

def send_slack_alert(level):
    """Send alert message to Slack"""
    message = {
        "text": f"⚠️ *Battery Alert!* {DEVICE_NAME} battery is at {level}%."
    }
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        if response.status_code == 200:
            print("✅ Slack alert sent.")
        else:
            print(f"❌ Failed to send Slack alert: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending alert: {e}")

def main():
    level = get_battery_level()
    if level is None:
        return
    print(f"Battery level: {level}%")
    if level < THRESHOLD:
        send_slack_alert(level)
    else:
        print("🔋 Battery level is fine.")

if __name__ == "__main__":
    main()
```



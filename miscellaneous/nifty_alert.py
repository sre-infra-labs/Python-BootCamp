#!/usr/bin/env python3
import argparse
import json
import tempfile
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from nsepython import index_history

# ----------------------------
# INDEX SYMBOLS FOR NSEPYTHON
# ----------------------------
NSE_INDEX_MAP = {
    "NIFTY 50": "NIFTY 50",
    "NIFTY NEXT 50": "NIFTY NEXT 50",
    "NIFTY MIDCAP 150": "NIFTY MIDCAP 150",
    "NIFTY MIDCAP SELECT": "NIFTY MIDCAP SELECT",
    "NIFTY SMALLCAP 250": "NIFTY SMALLCAP 250",
    "NIFTY SMALLCAP 50": "NIFTY SMALLCAP 50",
    "NIFTY 100": "NIFTY 100",
    "NIFTY 200": "NIFTY 200",
    "NIFTY 500": "NIFTY 500"
}


# ------------------------------------------------
# FETCH OHLC DATA USING NSEPYTHON (30 DAYS)
# ------------------------------------------------
def fetch_index_history(index_name):
    print(f"[INFO] Fetching NSE data for {index_name} ...")

    end = datetime.now()
    start = end - timedelta(days=30)

    df = index_history(
        start_date=start.strftime("%d-%m-%Y"),
        end_date=end.strftime("%d-%m-%Y"),
        index=index_name
    )

    if df is None or df.empty:
        raise Exception("NSE returned empty data")

    return df


# ------------------------------------------------
# CREATE MATPLOTLIB PLOT
# ------------------------------------------------
def create_plot(df, index_name):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Close"], label="Close Price")
    plt.title(f"{index_name} - Last 30 Days")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()

    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(tmpfile.name, format="png", dpi=200)
    plt.close()
    return tmpfile.name


# ------------------------------------------------
# POST TO SLACK
# ------------------------------------------------
def post_to_slack(webhook, text, image_path):
    print("[INFO] Sending Slack Alert...")

    # Upload image first
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    response = requests.post(
        webhook,
        data=json.dumps({"text": text}),
        headers={"Content-Type": "application/json"}
    )

    if not response.ok:
        print("[ERROR] Slack Webhook Failed:", response.text)
    else:
        print("[INFO] Slack Message Sent Successfully.")


# ------------------------------------------------
# MAIN
# ------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--webhook", required=True)
    parser.add_argument("--index", required=True)
    args = parser.parse_args()

    index_name = args.index.upper()
    if index_name not in NSE_INDEX_MAP:
        raise Exception(f"Index not supported: {index_name}")

    df = fetch_index_history(NSE_INDEX_MAP[index_name])

    # Today's data
    today = df.iloc[-1]
    high = today["High"]
    low = today["Low"]
    ltp = today["Close"]
    open_price = today["Open"]

    direction = "GREEN 🔼" if ltp >= open_price else "RED 🔽"

    msg = (
        f"*{index_name} Alert*\n"
        f"• Open: {open_price}\n"
        f"• High: {high}\n"
        f"• Low: {low}\n"
        f"• LTP: {ltp}\n"
        f"• Trend: {direction}"
    )

    # create chart
    chart_path = create_plot(df, index_name)

    # send Slack alert
    post_to_slack(args.webhook, msg, chart_path)

    print("[INFO] Completed.")


if __name__ == "__main__":
    main()


# python3 nifty_alert.py --index "NIFTY SMALLCAP 250" --webhook https://hooks.slack.com/services/XXXX/YYYY/ZZZZ


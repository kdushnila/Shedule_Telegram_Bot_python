import pandas as pd
import requests
from datetime import datetime, timedelta
import time


BOT_TOKEN: str = 'Your bot token'


def schedule_function():
    while True:
        sheet_id = "ID of your sheet"

        url_1 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

        df = pd.read_csv(url_1)
        df["Schedule DateTime"] = pd.to_datetime(df["Schedule DateTime"])

        previous_minute = datetime.now() - timedelta(minutes=1)
        current_time = datetime.now()
        print(current_time)
        df = df.loc[(df["Schedule DateTime"] > previous_minute) & (df["Schedule DateTime"] < current_time)]

        def send_message(row):
            bot_id = 'Your bot token'
            chat_id = "Your chat id"
            message = row[0]
            url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={message}"
            print(message)

            return requests.get(url).json()

        if not df.empty:
            df['status'] = df.apply(send_message, axis=1)
        time.sleep(60)



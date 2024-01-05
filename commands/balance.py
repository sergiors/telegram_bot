import pandas as pd
from telebot import TeleBot
from datetime import date
from configs import TELEGRAM_BOT_TOKEN
from utils import currency

bot = TeleBot(TELEGRAM_BOT_TOKEN, threaded=False)


def _sum_month(filepath: str, month: int, year: int):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])

    month_df = df[(df['date'].dt.year == year) & (df['date'].dt.month <= month)]
    return month_df['unitprice'].sum()


def reply_balance(filepath: str, date: date, chat_id: str):
    val = _sum_month(filepath, month=date.month, year=date.year)
    bot.send_message(
        chat_id=chat_id,
        text=f'Até o momento o valor é *{currency(val)}*',
        parse_mode='Markdown',
    )

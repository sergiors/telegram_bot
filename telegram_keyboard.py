from enum import EnumType
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard(enum: EnumType):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(*[InlineKeyboardButton(x, callback_data=x) for x in enum])

    return markup

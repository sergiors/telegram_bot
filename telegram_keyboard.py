from enum import EnumType
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# from spread import Category, PaymentMethod


def keyboard(enum: EnumType):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(*[InlineKeyboardButton(x, callback_data=x) for x in enum])

    return markup


# def categories_keyboard():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(
#         InlineKeyboardButton(
#             Category.UTILITIES, callback_data=Category.UTILITIES
#         ),
#         InlineKeyboardButton(
#             Category.TRANSPORTATION, callback_data=Category.TRANSPORTATION
#         ),
#         InlineKeyboardButton(Category.FOOD, callback_data=Category.FOOD),
#         InlineKeyboardButton(Category.DRINK, callback_data=Category.DRINK),
#         InlineKeyboardButton(
#             Category.SHOPPING, callback_data=Category.SHOPPING
#         ),
#         InlineKeyboardButton(
#             Category.GROCERIES, callback_data=Category.GROCERIES
#         ),
#         InlineKeyboardButton(
#             Category.EDUCATION, callback_data=Category.EDUCATION
#         ),
#         InlineKeyboardButton(Category.HEALTH, callback_data=Category.HEALTH),
#         InlineKeyboardButton(Category.TRAVEL, callback_data=Category.TRAVEL),
#         InlineKeyboardButton(
#             Category.ENTERTAINMENT, callback_data=Category.ENTERTAINMENT
#         ),
#         InlineKeyboardButton(Category.HOUSING, callback_data=Category.HOUSING),
#         InlineKeyboardButton(Category.OTHERS, callback_data=Category.OTHERS),
#     )
#     return markup


# def payments_keyboard():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(
#         InlineKeyboardButton(
#             PaymentMethod.PIX, callback_data=PaymentMethod.PIX
#         ),
#         InlineKeyboardButton(
#             PaymentMethod.CASH, callback_data=PaymentMethod.CASH
#         ),
#         InlineKeyboardButton(
#             PaymentMethod.CREDIT_CARD, callback_data=PaymentMethod.CREDIT_CARD
#         ),
#         InlineKeyboardButton(
#             PaymentMethod.DEBIT_CARD, callback_data=PaymentMethod.DEBIT_CARD
#         ),
#         InlineKeyboardButton(
#             PaymentMethod.BANK_SLIP, callback_data=PaymentMethod.BANK_SLIP
#         ),
#     )
#     return markup

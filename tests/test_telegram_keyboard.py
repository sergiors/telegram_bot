from telegram_keyboard import keyboard
from spread import Category


def test_keyboard():
    markup = keyboard(Category)
    assert len(markup.keyboard) == 6

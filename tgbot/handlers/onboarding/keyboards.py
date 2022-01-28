from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON, HUSKY_BUTTON, GERMAN_SHEPHERD_BUTTON, AKITA_INU_BUTTON, \
    SHIBA_INU_BUTTON, RETRIEVER_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text, husky_button_text, \
    german_shepherd_button_text, akita_inu_button_text, shiba_inu_button_text, retriever_button_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        # InlineKeyboardButton(github_button_text, url="https://github.com/ohld/django-telegram-bot"),
        # InlineKeyboardButton(secret_level_button_text, callback_data=f'{SECRET_LEVEL_BUTTON}')
        InlineKeyboardButton(husky_button_text, callback_data=f'{HUSKY_BUTTON}'),
        InlineKeyboardButton(german_shepherd_button_text, callback_data=f'{GERMAN_SHEPHERD_BUTTON}'),
        InlineKeyboardButton(akita_inu_button_text, callback_data=f'{AKITA_INU_BUTTON}'),
        InlineKeyboardButton(shiba_inu_button_text, callback_data=f'{SHIBA_INU_BUTTON}'),
        InlineKeyboardButton(retriever_button_text, callback_data=f'{RETRIEVER_BUTTON}'),
    ]]

    return InlineKeyboardMarkup(buttons)

from telegram import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.handlers.onboarding.manage_data import RETRIEVER_BUTTON, SHIBA_INU_BUTTON, AKITA_INU_BUTTON, GERMAN_SHEPHERD_BUTTON, HUSKY_BUTTON
from tgbot.handlers.onboarding.static_text import husky_button_text, german_shepherd_button_text, akita_inu_button_text, \
    shiba_inu_button_text, retriever_button_text


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def show_breeds() -> InlineKeyboardMarkup:
    try:
        buttons = [[
            InlineKeyboardButton(husky_button_text, callback_data=f'{HUSKY_BUTTON}'),
            InlineKeyboardButton(german_shepherd_button_text, callback_data=f'{GERMAN_SHEPHERD_BUTTON}'),
            InlineKeyboardButton(akita_inu_button_text, callback_data=f'{AKITA_INU_BUTTON}'),
            InlineKeyboardButton(shiba_inu_button_text, callback_data=f'{SHIBA_INU_BUTTON}'),
            InlineKeyboardButton(retriever_button_text, callback_data=f'{RETRIEVER_BUTTON}'),
        ]]
        return InlineKeyboardMarkup(buttons)
    except Exception as ex:
        print(ex, flush=True)

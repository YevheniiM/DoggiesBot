from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SEND_DOGS_BUTTON, IDENTIFY_BREED_BUTTON


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton("Send me dogs 🐕", callback_data=f'{SEND_DOGS_BUTTON}'),
        InlineKeyboardButton("Identify the breed", callback_data=f'{IDENTIFY_BREED_BUTTON}')
    ]]
    return InlineKeyboardMarkup(buttons, resize_keyboard=True)

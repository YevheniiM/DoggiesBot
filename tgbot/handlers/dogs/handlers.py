from random import randint

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command
from tgbot.handlers.utils.info import extract_user_data_from_update


class DogsHandlers:
    PHOTOS_RANGES = {
        'husky': 300,
        'german_shepherd': 300,
        'akita_inu': 72,
        'shiba_inu': 92,
        'retriever': 1499,
    }

    def get_handler(self, breed: str):
        return getattr(DogsHandlers, breed)

    @staticmethod
    def get_doggies(update: Update, context: CallbackContext, breed):
        user_id = extract_user_data_from_update(update)['user_id']
        try:
            photo_id = randint(1, DogsHandlers.PHOTOS_RANGES[breed])
            with open(f'/media/images/{breed}/{breed}-{photo_id}.jpeg', 'rb') as photo:
                context.bot.send_photo(
                    user_id,
                    photo
                )
            print(f'sending {breed} to: ', user_id)
            context.bot.send_message(chat_id=user_id,
                                     text="One moooore",
                                     reply_markup=make_keyboard_for_start_command())
        except Exception as ex:
            print(ex)
            context.bot.send_message(chat_id=user_id,
                                     text="Try one more time",
                                     reply_markup=make_keyboard_for_start_command())

    @staticmethod
    def husky(update: Update, context: CallbackContext) -> None:
        DogsHandlers.get_doggies(update, context, breed='husky')

    @staticmethod
    def german_shepherd(update: Update, context: CallbackContext) -> None:
        DogsHandlers.get_doggies(update, context, breed='german_shepherd')

    @staticmethod
    def akita_inu(update: Update, context: CallbackContext) -> None:
        DogsHandlers.get_doggies(update, context, breed='akita_inu')

    @staticmethod
    def shiba_inu(update: Update, context: CallbackContext) -> None:
        DogsHandlers.get_doggies(update, context, breed='shiba_inu')

    @staticmethod
    def retriever(update: Update, context: CallbackContext) -> None:
        DogsHandlers.get_doggies(update, context, breed='retriever')

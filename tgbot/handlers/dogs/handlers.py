import os.path
from random import randint

from telegram import Update
from telegram.ext import CallbackContext

from ai.ai_logic.breed_prediction import predict_breed_transfer
from dtb.custom_storages import media_storage
from tgbot.handlers.dogs.keyboards import show_breeds
from tgbot.handlers.utils.info import extract_user_data_from_update
from django.conf import settings


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
            if settings.DEBUG:
                with open(os.path.join(settings.IMAGES_PATH, f'{breed}/{breed}-{photo_id}.jpeg'), 'rb') as photo:
                    context.bot.send_photo(
                        user_id,
                        photo
                    )
            else:
                with media_storage.open(os.path.join(settings.IMAGES_PATH, f'{breed}/{breed}-{photo_id}.jpeg'), "rb") as photo:
                    context.bot.send_photo(
                        user_id,
                        photo
                    )

            print(f'sending {breed} to: ', user_id)
            context.bot.send_message(chat_id=user_id,
                                     text="One mooore :)",
                                     reply_markup=show_breeds())
        except Exception as ex:
            print(ex)
            context.bot.send_message(chat_id=user_id,
                                     text="Try one more time",
                                     reply_markup=show_breeds())

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

    @staticmethod
    def show_dogs_breeds(update: Update, context: CallbackContext) -> None:
        user_id = extract_user_data_from_update(update)['user_id']
        context.bot.send_message(chat_id=user_id,
                                 text="Here are some breeds to choose from :)",
                                 reply_markup=show_breeds())

    @staticmethod
    def ask_for_photo(update: Update, context: CallbackContext) -> None:
        user_id = extract_user_data_from_update(update)['user_id']
        context.bot.send_message(chat_id=user_id,
                                 text="Send me the photo, please :)")

    @staticmethod
    def identify_breed(update: Update, context: CallbackContext) -> None:
        user_id = extract_user_data_from_update(update)['user_id']
        file = context.bot.get_file(update.message.photo[-1].file_id)
        bytes_photo = file.download_as_bytearray()
        breed = predict_breed_transfer(image=bytes_photo)
        print(f"Detected breed for user [{user_id}] request: {breed}")
        context.bot.send_message(chat_id=user_id,
                                 text=f"This is {breed} :)")

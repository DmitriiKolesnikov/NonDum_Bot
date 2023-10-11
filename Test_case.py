import os

from aiogram import Bot, Dispatcher, executor, types
import easyocr
import logging
import aiogram.utils.markdown as md


TOKEN_API = '6588390362:AAFp5cmoOWbN5tP4qj6nCSKuDKwmBnPdOWU'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


reader = easyocr.Reader(['en', 'ru'])  # Укажите нужные языки для OCR


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет! Я бот для распознавания текста на изображениях. Пришлите мне фотографию с текстом!")


# Обработчик фотографий
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def process_photo(message: types.Message):
    # Скачиваем фотографию
    photo = message.photo[-1]
    photo_path = f"photo_{photo.file_id}.jpg"
    await photo.download(photo_path)

    # Распознаем текст на фотографии
    result = reader.readtext(photo_path)
    text = "\n".join([res[1] for res in result])

    if not text:
        text = "Текст на фотографии не найден."

    # Отправляем распознанный текст в ответе
    await message.answer(md.text(text))
    os.remove(photo_path)


async def on_startup(_):
    print(f'Bot started')

    
if __name__ == "__main__":
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
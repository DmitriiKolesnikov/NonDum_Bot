
from aiogram import types, Bot, Dispatcher
import pytesseract
from PIL import Image

API_TOKEN = "6214205049:AAG2hKi_LViqSZuxbB37VMoyySSK3w7i2Fg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Отправь мне фотографию с текстом, и я попробую его извлечь.')

# Обработчик фотографий

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    # Получаем объект фотографии
    photo = message.photo[-1]

    # Сохраняем фотографию на диск
    await photo.download('image.jpg')

    # Открываем фотографию и извлекаем текст
    image = Image.open('image.jpg')
    text = pytesseract.image_to_string(image)

    # Отправляем извлеченный текст пользователю
    await message.reply(text)

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)

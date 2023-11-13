import os

from aiogram import Bot, Dispatcher, executor, types
import easyocr
import logging
from datetime import datetime


TOKEN_API = '6588390362:AAFp5cmoOWbN5tP4qj6nCSKuDKwmBnPdOWU'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


reader = easyocr.Reader(['en', 'ru'])


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def process_photo(message: types.Message):
    photo = message.photo[-1]
    photo_path = f"photo_{photo.file_id}.jpg"
    await photo.download(photo_path)
    result = reader.readtext(photo_path)
    list_from_text = ''
    text = "\n".join([i[1] for i in result])
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{text}')
    for i in result:
        list_from_text += i[1]
    os.remove(photo_path)
    num = ''
    num_list = []
    for char in list_from_text:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year


    if 3000 in num_list or '3000 ₽' in text or '3 ООО ₽' in text or '3000.00' in text or '3 000.00 p.' in text or \
            '3 000.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 3000 рублей\n')
        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 3000 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

    elif 2000 in num_list or '2000 ₽' in text or '2 ООО ₽' in text or '2000.00' in text or '2 000.00 p.' in text or \
            '2 000.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2000 рублей\n')
        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2000 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

    elif 2500 in num_list or '2500 ₽' in text or '2 5ОО ₽' in text or '2500.00' in text or '2 500.00 p.' in text or \
            '2 500.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2500 рублей\n')
        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2500 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

    elif 2500 in num_list or '2400 ₽' in text or '2 4ОО ₽' in text or '2400.00' in text or '2 400.00 p.' in text or \
            '2 400.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2400 рублей\n')
        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2400 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, ваша заявка находится на '
                                    f'рассмотрении.\n'
                                    f'Ожидайте ответа от технической поддержки.')
        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, произошла ошибка во время оплаты: невозможно проверить'
                                     f'действительность оплаты.\n'
                                     f'Данные о пользователе:\n'
                                     f'Ник в Телеграм: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

    os.remove(photo_path)


async def on_startup(_):
    print(f'Bot started')


print(datetime.now().day)
print((datetime.now().month))
print(datetime.now().year)
print(type(datetime.now().day))
print(type((datetime.now().month)))

    
if __name__ == "__main__":
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
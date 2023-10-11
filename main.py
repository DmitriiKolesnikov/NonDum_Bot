from aiogram import Bot, Dispatcher, executor, types
from openpyxl import Workbook
from All_text import *
from Main_kb import *


TOKEN_API = '6588390362:AAFp5cmoOWbN5tP4qj6nCSKuDKwmBnPdOWU'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


wb = Workbook()
ws = wb.active
user_id_list = ['id_пользователя']
user_name_list = ['Имя пользователя']
registration_data_list = ['Дата регистрации пользователя']
price_list = ['Сумма покупок с комиссией']
commission_list = ['Величина комисси']
final_price_list = ['Итоговая сумма']
admin_list = ['Админ']
main_columns_name_data = [user_id_list,
                          user_name_list,
                          registration_data_list,
                          price_list,
                          commission_list,
                          final_price_list,
                          admin_list]

for row in main_columns_name_data:
    ws.append(row)


async def on_startup(_):
    print(f'Bot started')


@dp.message_handler(commands=['start'])
async def start_command(m: types.Message) -> None:
    start_photo_link = open('main_photo.png', 'rb')
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=start_photo_link,
                         caption=start_text)
    await bot.send_message(chat_id=m.from_user.id,
                           text=name_text)
    await m.delete()


@dp.message_handler(commands=['description'])
async def description_command(m: types.Message) -> None:
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=description_photo_link,
                         caption=description_text,
                         parse_mode="HTML")
    await m.delete()


@dp.message_handler(text='Помощь в учебе')
async def help_in_studying(m: types.Message) -> None:
    list_of_courses = ['Первый курс', 'Второй курс']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*list_of_courses)
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=help_in_studying_photo,
                         caption=help_instudying_text,
                         parse_mode="HTML",
                         reply_markup=studying_main_kb)
    await m.delete()


@dp.message_handler(text='🍾Nondum Party')
async def tusovki_command(m: types.Message) -> None:
    tusovki_photo = open('tusovki.png', 'rb')
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=tusovki_photo,
                         caption=tusovki_text,
                         parse_mode="HTML",
                         reply_markup=tusovki_kb)
    await m.delete()


@dp.message_handler(text='Заказы одежды с Poizon')
async def orders_from_poizon(m: types.Message) -> None:
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=orders_from_poizon_photo,
                         caption=orders_from_poizon_text,
                         parse_mode="HTML",
                         reply_markup=poison_kb)
    await m.delete()


@dp.message_handler()
async def words_handler(m: types.Message):
    message = m.text.split()
    if len(message) == 2 and m.text.istitle():
        if m.from_user.id not in user_id_list:
            user_id_list.append(m.from_user.id)
            user_name_list.append(m.text)
            wb.save("Nondum_clients.xlsx")
        else:
            pass
        await bot.send_message(chat_id=m.from_user.id,
                               text=f"Приятно познакомиться, {m.from_user.full_name}, теперь мне понадобиться твой "
                                    f"телефон, чтобы всегда оставаться на связи!",)
    await m.delete()


@dp.callback_query_handler()
async def work_with_text_command(callback: types.CallbackQuery) -> None:
    if callback.data == 'first_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_first_course_text,
                               parse_mode="HTML",
                               reply_markup=studying_first_kb)
        await callback.message.delete()

    elif callback.data == 'second_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_second_course_text,
                               parse_mode="HTML",
                               reply_markup=studying_second_kb)
        await callback.message.delete()

    elif callback.data == 'files_first_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_files_first_course_text,
                               parse_mode="HTML",
                               reply_markup=subjects_first_kb)
        await callback.message.delete()

    elif callback.data == 'lessons_first_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_lessons_first_course_text,
                               parse_mode="HTML",
                               reply_markup=lessons_first_kb)
        await callback.message.delete()

    elif callback.data == 'matan_first':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_matan_first_text,
                               parse_mode="HTML",
                               reply_markup=types_of_lessons_first_matan_kb)
        await callback.message.delete()

    elif callback.data == 'linal_first':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_linal_first_text,
                               parse_mode="HTML",
                               reply_markup=types_of_lessons_first_linal_kb)
        await callback.message.delete()

    elif callback.data == 'files_second_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_files_second_course_text,
                               parse_mode="HTML",
                               reply_markup=subjects_second_kb)
        await callback.message.delete()

    elif callback.data == 'lessons_second_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_lessons_second_course_text,
                               parse_mode="HTML",
                               reply_markup=lessons_second_kb)
        await callback.message.delete()

    elif callback.data == 'individual_first_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_individual_first_m_text,
                               parse_mode="HTML",
                               reply_markup=types_of_individual_lessons_first_matan_kb)
        await callback.message.delete()

    elif callback.data == 'individual_first_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_individual_first_l_text,
                               parse_mode="HTML",
                               reply_markup=types_of_individual_lessons_first_linal_kb)
        await callback.message.delete()

    elif callback.data == 'group_first_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_group_first_m_text,
                               parse_mode="HTML",
                               reply_markup=types_of_group_lessons_first_matan_kb)
        await callback.message.delete()

    elif callback.data == 'group_first_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=callback_group_first_l_text,
                               parse_mode="HTML",
                               reply_markup=types_of_group_lessons_first_linal_kb)
        await callback.message.delete()

if __name__ == "__main__":
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)

print(user_id_list)
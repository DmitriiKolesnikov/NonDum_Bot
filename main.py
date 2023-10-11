from aiogram import Bot, Dispatcher, executor, types
from openpyxl import Workbook
from datetime import datetime
from All_text import *
from Main_kb import *
from Google_sheet import *


TOKEN_API = '6588390362:AAFp5cmoOWbN5tP4qj6nCSKuDKwmBnPdOWU'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


## 905449479 - Ника Осадчева
## 5490940595 - Даня Мальцев


wb = Workbook()
ws = wb.active
user_id_list = ['id_пользователя']
user_name_list = ['Имя пользователя']
registration_data_list = ['Дата регистрации пользователя']
ticket_price_list = ['Сумма покупок билетов']
poizon_price_list = ['Сумма  покупок на пойзоне']
commission_list = ['Величина комисси']
final_price_list = ['Итоговая сумма']
admin_list = ['Роль пользователя']
list_of_admins_id = [683092826, 5490940595, 905449479]
promo_list_10_percent = ['dfuTvxe', 'taEm2hQ', 'lKhyJWt', '7ug0avp', 'JA97V17', 'UbCyFsu', 'PFIpAMc', 'Fz48DBY',
                         's1UqXAk', 'fKB4wbQ', 'xWuEG7S', '04yxkqn', '7OJwFPB', 'wF7AvHI', 'XliL9Za', '4tbOWGz',
                         'aDQMnZY', 'kKzMlvh', 'Buq5PRS', 'l7EkUpZ', 'kSzaVQw', 'ueMHa8c', 'KmDaBvS', 'rl7XLR9',
                         'Ym83cc8', 'M07aRQl', 'PsxhOO9', 'Vz5bMuk', 'UlJJNZz', 'yJ5bzHM', 'Wumyq70', 'sn9uAP4',
                         'GwgNJeT', 'loRRMhj', 'ZW3k8Vf', 'L9fwB7z', '1c5Gr8m', 'TZQ8UsD', '1svcWa2', '4ZuCV7N',
                         '8bhL4hp', 'xVR4ENw', 'hP5H5cK', 'd7Cjb3U', 'LUyqard', 'zI9t5g1', 'GeP692A', 'NTswAGT',
                         'zECBqA2', 'cow4G7q']

# Setup prices


async def on_startup(_):
    print(f'Bot started')


@dp.message_handler(commands=['start'])
async def start_command(m: types.Message) -> None:
    start_photo_link = open('main_photo.png', 'rb')
    values_id_list = worksheet.col_values(1)

    if str(m.from_user.id) not in values_id_list:
        user_name = m.from_user.full_name
        current_time = str(datetime.now().date())
        if m.from_user.id in list_of_admins_id:
            users_role = 'Админ'
            list_of_main_google_info = [m.from_user.id, user_name, users_role, current_time]
            worksheet.append_row(list_of_main_google_info)
        else:
            users_role = 'Пользователь'
            list_of_main_google_info = [m.from_user.id, user_name, users_role, current_time]
            worksheet.append_row(list_of_main_google_info)
    else:
        pass

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
    main_columns_name_data = [user_id_list,
                              user_name_list,
                              registration_data_list,
                              ticket_price_list,
                              poizon_price_list,
                              commission_list,
                              final_price_list,
                              admin_list]

    if len(message) == 2 and m.text.istitle():
        if m.from_user.id not in user_id_list:
            user_id_list.append(str(m.from_user.id))
            user_name_list.append(m.text)
            current_date = datetime.now().date()
            registration_data_list.append(str(current_date))
            if m.from_user.id in list_of_admins_id:
                admin_list.append('Админ')
            elif m.from_user.id not in list_of_admins_id:
                admin_list.append('Пользователь')
            for row in main_columns_name_data:
                ws.append(row)
            wb.save("Nondum_clients.xlsx")
        else:
            pass
        await bot.send_message(chat_id=m.from_user.id,
                               text=f"Приятно познакомиться, {m.text}",
                               reply_markup=kb_main)
        await bot.send_message(chat_id=5490940595,
                               text=f'Уважаемый Даниил, к вам запсался новый пользователь по имени {m.text}')

    elif len(message) == 2 and m.text == 'Скинь эксель' or m.text == 'Скинь exel':
        await m.reply_document(open('Nondum_clients.xlsx', 'rb'))
        await m.delete()

    elif len(message) == 1 and len(message[0]) == 7 and message[0] in promo_list_10_percent:
        promo_list_10_percent.remove(message[0])
        print(len(promo_list_10_percent))
        current_time = datetime.now()
        if current_time < datetime.strptime('2023-10-29', "%Y-%m-%d"):
            buttons = [
               InlineKeyboardButton(text='Оплатить 2000Р', callback_data='payment_ticket_2000')
            ]
            keyboard = InlineKeyboardMarkup().row(*buttons)
            await bot.send_message(chat_id=m.from_user.id,
                                   text=f'Для произведения оплаты нажмите на «Оплатить 2000Р»',
                                   parse_mode="HTML",
                                   reply_markup=keyboard)
        elif current_time >= datetime.strptime('2023-10-29', "%Y-%m-%d"):
            buttons = [
               InlineKeyboardButton(text='Оплатить 2400Р', callback_data='payment_ticket_2400')
            ]
            keyboard = InlineKeyboardMarkup().row(*buttons)
            await bot.send_message(chat_id=m.from_user.id,
                                   text=f'Для произведения оплаты нажмите на «Оплатить 2400Р»',
                                   parse_mode="HTML",
                                   reply_markup=keyboard)
        await m.delete()

    elif len(message) == 1 and len(message[0]) == 7 and message[0] not in promo_list_10_percent:
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'К сожалению, данный промокод уже был использован. Попробуйте ввести другой',
                               parse_mode="HTML")
        await m.delete()


@dp.callback_query_handler()
async def work_with_text_command(callback: types.CallbackQuery) -> None:
    if callback.data == 'parties':
        await bot.send_photo(chat_id=callback.from_user.id,
                             caption=halloween_text_1,
                             photo='https://sun1-93.userapi.com/impg/Rjd-QEhjB1t5dqyM_NmUnvucvmRcpRKWOfkDmw/uoGUzOvTivQ'
                                   '.jpg?size=1179x763&quality=95&sign=4bea81681410334210ce538df26d36b8&type=album',
                             parse_mode="HTML")
        await bot.send_message(chat_id=callback.from_user.id,
                               text=halloween_text_2,
                               parse_mode="HTML",
                               reply_markup=buy_ticket_kb)

    elif callback.data == 'first_course':
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

    elif callback.data == 'buy':
        current_time = datetime.now()
        if current_time < datetime.strptime('2023-10-29', "%Y-%m-%d"):
            buy_buttons_first = [
                InlineKeyboardButton('Оплатить 2500Р', callback_data='payment_tickets_2500'),
                InlineKeyboardButton('Воспользоваться промокодом', callback_data='promo')
            ]
            buy_kb = InlineKeyboardMarkup().row(*buy_buttons_first)
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'для совешения покупки, нажмите на кнопку «Оплатить 2500Р».\n\n'
                                        f'Если вы имеете промокод для скидки, то нажите на кнопку:\n'
                                        f'«Воспользоваться промокодом»',
                                   parse_mode="HTML",
                                   reply_markup=buy_kb)
        if current_time > datetime.strptime('2023-10-29', "%Y-%m-%d"):
            buy_buttons = [
                InlineKeyboardButton('Оплатить 3000Р', callback_data='payment_tickets_3000'),
                InlineKeyboardButton('Воспользоваться промокодом', callback_data='promo')
            ]
            buy_kb = InlineKeyboardMarkup().row(*buy_buttons)
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'для совешения покупки, нажмите на кнопку «Оплатить 2500Р».\n\n'
                                        f'Если вы имеете промокод для скидки, то нажите на кнопку:\n'
                                        f'«Воспользоваться промокодом»',
                                   parse_mode="HTML",
                                   reply_markup=buy_kb)

    elif callback.data == 'promo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Введите промокод, который вы получили от организаторов',
                               parse_mode="HTML")


if __name__ == "__main__":
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)

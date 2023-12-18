from aiogram import Bot, Dispatcher, executor, types
import os
import easyocr
import logging
from datetime import datetime
from All_text import *
from Main_kb import *
from Google_sheet import *


TOKEN_API = '6588390362:AAFp5cmoOWbN5tP4qj6nCSKuDKwmBnPdOWU'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


reader = easyocr.Reader(['en', 'ru'])


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## 905449479 - Ника Осадчева
## 5490940595 - Даня Мальцев
## 317434662 - Максимилиан Радзевич


list_of_admins_id = ['683092826', '5490940595', '905449479', '317434662', '773416334']
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

            await bot.send_photo(chat_id=m.from_user.id,
                                 photo=start_photo_link,
                                 caption=start_text,
                                 reply_markup=kb_main_admins)

        else:
            users_role = 'Пользователь'
            list_of_main_google_info = [m.from_user.id, user_name, users_role, current_time]
            worksheet.append_row(list_of_main_google_info)

            await bot.send_photo(chat_id=m.from_user.id,
                                 photo=start_photo_link,
                                 caption=start_text,
                                 reply_markup=kb_main)

        await bot.send_message(chat_id=5490940595,
                               text=f'Даниил, в вашей сиситеме зарегистрировался новый пользователь:\n\n'
                                    f'Ник пользователя в Телеграм: @{m.from_user.full_name}\n'
                                    f'Дата регистрации: {datetime.now().date()}'
                                    f'Роль пользователя: {list_of_main_google_info[2]}')

    else:
        if str(m.from_user.id) in list_of_admins_id:
            await bot.send_photo(chat_id=m.from_user.id,
                                 photo=start_photo_link,
                                 caption=start_text,
                                 reply_markup=kb_main_admins)
        else:
            await bot.send_photo(chat_id=m.from_user.id,
                                 photo=start_photo_link,
                                 caption=start_text,
                                 reply_markup=kb_main)

    await m.delete()


@dp.message_handler(commands=['description'])
async def description_command(m: types.Message) -> None:
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=description_photo_link,
                         caption=description_text,
                         parse_mode="HTML")
    await m.delete()


@dp.message_handler(text='🎒Помощь в учебе')
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


@dp.message_handler(text='👟Заказы одежды с Poizon')
async def orders_from_poizon(m: types.Message) -> None:
    await bot.send_photo(chat_id=m.from_user.id,
                         photo=orders_from_poizon_photo,
                         caption=orders_from_poizon_text,
                         parse_mode="HTML",
                         reply_markup=poison_kb)
    await m.delete()


@dp.message_handler(text='Ссылка на гугл таблицу')
async def google_link(m: types.Message):
    await bot.send_message(chat_id=m.from_user.id,
                           text=f"Уважаемый <b>{m.from_user.full_name}</b>, вам представлена ссылка на"
                                f" Google таблицу\n\n"
                                f"https://docs.google.com/spreadsheets/d/1WNjLQIbB0yfUQcu6Wy154PtCHouhp_ZvCBJ"
                                f"5FWXUTtY/edit?usp=sharing",
                           parse_mode="HTML")

    await m.delete()


@dp.message_handler(text='Список админов')
async def admins_list_command(m: types.Message):
    await bot.send_message(chat_id=m.from_user.id,
                           text=f'Уважаемый {m.from_user.full_name}, вам представлен список админов: \n\n'
                                f'Никнейм пользователя - @Jim Kolesnikov\n\n'
                                f'Никнейм пользователя - @m.r.\n\n'
                                f'Никнейм пользователя - @Turgen4ik\n\n'
                                f'Никнейм пользователя - @слим из группы центр\n\n'
                                f'Никнейм пользвателя - @Losocb',
                           parse_mode="HTML")

    await m.delete()


@dp.message_handler()
async def words_handler(m: types.Message):

    message = m.text.split()

    if len(message) == 1 and len(message[0]) == 7 and message[0] in promo_list_10_percent:
        promo_list_10_percent.remove(message[0])
        current_time = datetime.now()
        if current_time < datetime.strptime('2023-12-16', "%Y-%m-%d"):
            buttons = [
               InlineKeyboardButton(text='Оплатить 2250Р', callback_data='payment_ticket_2000')
            ]
            keyboard = InlineKeyboardMarkup().row(*buttons)
            await bot.send_message(chat_id=m.from_user.id,
                                   text=f'Для произведения оплаты нажмите на «Оплатить 2250Р»',
                                   parse_mode="HTML",
                                   reply_markup=keyboard)
        elif current_time >= datetime.strptime('2023-12-16', "%Y-%m-%d"):
            buttons = [
               InlineKeyboardButton(text='Оплатить 2500Р', callback_data='payment_ticket_2400')
            ]
            keyboard = InlineKeyboardMarkup().row(*buttons)
            await bot.send_message(chat_id=m.from_user.id,
                                   text=f'Для произведения оплаты нажмите на «Оплатить 2500Р»',
                                   parse_mode="HTML",
                                   reply_markup=keyboard)
        await m.delete()

    elif len(message) == 1 and len(message[0]) == 7 and message[0] not in promo_list_10_percent:
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'К сожалению, данный промокод <b>уже был использован</b> '
                                    f'или такого <b>не существует</b>. \n\nПопробуйте ввести другой',
                               parse_mode="HTML")
        await m.delete()


@dp.callback_query_handler()
async def work_with_text_command(callback: types.CallbackQuery) -> None:
    if callback.data == 'parties':
        await bot.send_photo(chat_id=callback.from_user.id,
                             caption=halloween_text_1,
                             photo='https://sun1-21.userapi.com/impf/Q1eSnTcGECj3kiJbFcoV8u3CV7Q4vA2TojWf5g/kx_k2bcIVJ'
                                   'c.jpg?size=1024x1024&quality=96&sign=f60d8e76a856159a1e585d03be093568&c_uniq_tag='
                                   'oz_yuVEL-P4YWxR2Fopqr_wgsRBXvMjJy0I8rZPasJ8&type=album',
                             parse_mode="HTML")
        await bot.send_message(chat_id=callback.from_user.id,
                               text=halloween_text_2,
                               parse_mode="HTML",
                               reply_markup=buy_ticket_kb)

        await callback.message.delete()

    elif callback.data == 'buy':
        current_time = datetime.now()
        if current_time < datetime.strptime('2023-12-16', "%Y-%m-%d"):
            buy_buttons_first = [
                InlineKeyboardButton('Оплатить 2750Р', callback_data='payment_tickets_2500'),
                InlineKeyboardButton('Промокод', callback_data='promo')
            ]
            buy_kb = InlineKeyboardMarkup().row(*buy_buttons_first)
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'для совешения покупки, нажмите на кнопку «Оплатить 2750Р».\n\n'
                                        f'Если вы имеете промокод для скидки, то нажите на кнопку:\n'
                                        f'«Промокод»',
                                   parse_mode="HTML",
                                   reply_markup=buy_kb)
        if current_time > datetime.strptime('2023-12-16', "%Y-%m-%d"):
            buy_buttons = [
                InlineKeyboardButton('Оплатить 3000Р', callback_data='payment_tickets_3000'),
                InlineKeyboardButton('Промокод', callback_data='promo')
            ]
            buy_kb = InlineKeyboardMarkup().row(*buy_buttons)
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'для совешения покупки, нажмите на кнопку «Оплатить 3000Р».\n\n'
                                        f'Если вы имеете промокод для скидки, то нажите на кнопку:\n'
                                        f'«Промокод»',
                                   parse_mode="HTML",
                                   reply_markup=buy_kb)

        await callback.message.delete()

    elif callback.data == 'promo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Введите промокод, который вы получили от организаторов',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == 'first_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены <b>материлы</b> для самостоятельной подготовки и <b>занятия с '
                                    f'преподавателем</b> '
                                    f'по выбранным дисциплинам: \n\n<b>Математический анализ,\nЛинейная алгебра,\n'
                                    f'Экономическая география,\nВведение в экономику.</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode="HTML",
                               reply_markup=studying_first_kb)

        await callback.message.delete()

    elif callback.data == 'second_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены <b>занятие с '
                                    f'преподавателем</b> '
                                    f'по выбранным дисциплинам: \n\n<b>Математическая статистика,\nМикроэкономика,\n'
                                    f'Макроэкономика,\nДемография.</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode="HTML",
                               reply_markup=lessons_second_kb)

        await callback.message.delete()

    elif callback.data == 'files_first_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены <b>материлы</b> для самостоятельной подготовки '
                                    f'по выбранным дисциплинам: \n\n<b>Математический анализ\nЛинейная алгебра\n'
                                    f'Экономическая география\nВведение в экономику</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее.\n'
                                    f'После клика, с вами свяжется наше контакное лицо',
                               parse_mode="HTML",
                               reply_markup=subjects_first_kb)

        await callback.message.delete()

    elif callback.data == 'matan_first_s':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, ваша заявка о '
                                    f'самостоятельном '
                                    f'прохождении курса успешно отправлена, в скором времени с вами свяжется '
                                    f'преподавтель. \n\n Успехов в учебе!',
                               parse_mode="HTML")

        await bot.send_message(chat_id=317434662,
                               text=f'Уважаемый, Максимилиан, у вас появилась заявка на доступ к материалам для '
                                    f'самомтоятельной подготовки. Данные заявки:\n\n'
                                    f'Имя в Телеграме: <b>{callback.from_user.full_name}</b>,\n'
                                    f'Дата подачи заявки: <b>{datetime.now().date()}</b>, \n'
                                    f'Выбранный предмет: <b>математический анализ</b>',
                               parse_mode='HTML')

    elif callback.data == 'linal_first_s':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, ваша заявка о '
                                    f'самостоятельном '
                                    f'прохождении курса успешно отправлена, в скором времени с вами свяжется '
                                    f'преподавтель. \n\n Успехов в учебе!',
                               parse_mode="HTML")

        await bot.send_message(chat_id=317434662,
                               text=f'Уважаемый, Максимилиан, у вас появилась заявка на доступ к материалам для '
                                    f'самомтоятельной подготовки. Данные заявки:\n\n'
                                    f'Имя в Телеграме: <b>{callback.from_user.full_name}</b>,\n'
                                    f'Дата подачи заявки: <b>{datetime.now().date()}</b>, \n'
                                    f'Выбранный предмет: <b>линейная алгебра</b>',
                               parse_mode='HTML')

        await callback.message.delete()

    elif callback.data == 'ekgeo_first_s':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, ваша заявка о '
                                    f'самостоятельном '
                                    f'прохождении курса успешно отправлена, в скором времени с вами свяжется '
                                    f'преподавтель. \n\n Успехов в учебе!',
                               parse_mode="HTML")

        await bot.send_message(chat_id=317434662,
                               text=f'Уважаемый, Максимилиан, у вас появилась заявка на доступ к материалам для '
                                    f'самомтоятельной подготовки. Данные заявки:\n\n'
                                    f'Имя в Телеграме: <b>{callback.from_user.full_name}</b>,\n'
                                    f'Дата подачи заявки: <b>{datetime.now().date()}</b>, \n'
                                    f'Выбранный предмет: <b>экономическая география</b>',
                               parse_mode='HTML')

        await callback.message.delete()

    elif callback.data == 'vvek_first_s':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, ваша заявка о '
                                    f'самостоятельном '
                                    f'прохождении курса успешно отправлена, в скором времени с вами свяжется '
                                    f'преподавтель. \n\n Успехов в учебе!',
                               parse_mode="HTML")

        await bot.send_message(chat_id=317434662,
                               text=f'Уважаемый, Максимилиан, у вас появилась заявка на доступ к материалам для '
                                    f'самомтоятельной подготовки. Данные заявки:\n\n'
                                    f'Имя в Телеграме: <b>{callback.from_user.full_name}</b>,\n'
                                    f'Дата подачи заявки: <b>{datetime.now().date()}</b>, \n'
                                    f'Выбранный предмет: <b>введение в экономику/b>',
                               parse_mode='HTML')

        await callback.message.delete()

    elif callback.data == 'lessons_first_course':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены предметы для изучения:'
                                    f' \n\n<b>Математический анализ</b>\n<b>Линейная алгебра</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode="HTML",
                               reply_markup=lessons_first_kb)
        await callback.message.delete()

    elif callback.data == 'matan_first':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены способы заниматься математическим анализом с преподавателем:'
                                    f' \n\n<b>Индивидуально</b>\n<b>в Группе</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode="HTML",
                               reply_markup=types_of_lessons_first_matan_kb)

        await callback.message.delete()

    elif callback.data == 'linal_first':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены способы заниматься линейной алгеброй с преподавателем:'
                                    f' \n\n<b>Индивидуально</b>\n<b>В группе</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode="HTML",
                               reply_markup=types_of_lessons_first_linal_kb)

        await callback.message.delete()

    elif callback.data == 'individual_first_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>индивидуальные</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>2100</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>5500</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>11000</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>16500</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>21900</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode="HTML",
                               reply_markup=types_of_individual_lessons_first_matan_kb)
        await callback.message.delete()

    elif callback.data == 'individual_first_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>индивидуальные</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>2100</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>5500</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>11000</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>16500</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>21900</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode="HTML",
                               reply_markup=types_of_individual_lessons_first_linal_kb)
        await callback.message.delete()

    elif callback.data == 'group_first_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>групповые</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>1000</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>2900</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>5600</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>839000</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>10990</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode="HTML",
                               reply_markup=types_of_group_lessons_first_matan_kb)
        await callback.message.delete()

    elif callback.data == 'group_first_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>групповые</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>1000</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>2900</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>5600</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>839000</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>10990</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode="HTML",
                               reply_markup=types_of_group_lessons_first_linal_kb)
        await callback.message.delete()

    elif callback.data == 'matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены способы заниматься математической статистикой с преподавателем:'
                                    f' \n<b>индивидуально</b> или <b>в группе</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode='HTML',
                               reply_markup=types_of_lessons_second_matstat_kb)

    elif callback.data == 'individual_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>индивидуальные</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>2100</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>5500</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>11000</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>16500</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>21900</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_individual_lessons_second_matstat_kb)

    elif callback.data == 'group_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>групповые</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>1000</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>2900</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>5600</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>839000</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>10990</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_group_lessons_second_matstat_kb)

    elif callback.data == 'mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены способы заниматься микроэкономикой с преподавателем:'
                                    f' \n<b>индивидуально</b> или <b>в группе</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode='HTML',
                               reply_markup=types_of_lessons_second_mikra_kb)

    elif callback.data == 'individual_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>индивидуальные</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>2100</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>5500</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>11000</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>16500</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>21900</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_individual_lessons_second_mikra_kb)

    elif callback.data == 'group_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>групповые</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>1000</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>2900</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>5600</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>839000</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>10990</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_group_lessons_second_mikra_kb)

    elif callback.data == 'makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены способы заниматься макроэкономикой с преподавателем:'
                                    f' \n<b>индивидуально</b> или <b>в группе</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode='HTML',
                               reply_markup=types_of_lessons_second_makra_kb)

    elif callback.data == 'individual_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>индивидуальные</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>2100</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>5500</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>11000</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>16500</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>21900</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_individual_lessons_second_makra_kb)

    elif callback.data == 'group_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>групповые</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>1000</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>2900</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>5600</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>839000</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>10990</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_group_lessons_second_makra_kb)

    elif callback.data == 'demograf':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены способы заниматься демографией с преподавателем:'
                                    f' \n<b>индивидуально</b> или <b>в группе</b>\n\n'
                                    f'Чтобы выбрать интересующая вас опцию, достаточно кликнуть на нее)',
                               parse_mode='HTML',
                               reply_markup=types_of_lessons_second_demo_kb)

    elif callback.data == 'individual_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>индивидуальные</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>2100</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>5500</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>11000</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>16500</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>21900</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_individual_lessons_second_demo_kb)

    elif callback.data == 'group_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, в данном разделе вам '
                                    f'представлены рассценки на <b>групповые</b> занятия с преподавателем:\n\n'
                                    f'<b>Одно</b> занятие - <b>1000</b> рублей\n'
                                    f'<b>Три</b> занятия - <b>2900</b> рублей\n'
                                    f'<b>Шесть</b> занятий - <b>5600</b> рублей\n'
                                    f'<b>Девять</b> занятий - <b>839000</b> рублей\n'
                                    f'<b>Двеннадцать</b> занятий - <b>10990</b> рублей\n\n'
                                    f'Чтобы выбрать интересующую вас опцию, достаточно кликнуть на нее. После '
                                    f'подтверждения оплаты с вами свяжется преподаватель.\n\n'
                                    f'Успехов в обучении!)',
                               parse_mode='HTML',
                               reply_markup=types_of_group_lessons_second_demo_kb)

    elif callback.data == 'payment_ticket_2000':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2250р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2250 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79998849383</b>\n\n'
                                    f'Тинькофф',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == 'payment_ticket_2400':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79998849383</b>\n\n'
                                    f'Тинькофф',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == 'payment_tickets_3000':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>3000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>3000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79998849383</b>\n\n'
                                    f'Тинькофф',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == 'payment_tickets_2500':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2750р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2750 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79998849383</b>\n\n'
                                    f'Тинькофф',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_f_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5500_f_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '11000_f_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>11000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '16500_f_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>16500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>16500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '21900_f_m':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>21900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>21900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_f_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5500_f_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '11000_f_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>11000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '16500_f_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>16500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>16500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '21900_f_l':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>21900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>21900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '1000_m_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>1000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>1000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_m_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5501_m_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '8390_m_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>8390р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>8390 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '10990_m_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>10990р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>10990 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '1000_l_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату групповых занятий по матану. <b>Сумма перевода</b> '
                                    f'должна составлять <b>1000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегодняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>1000 рублей</b>,\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_l_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5501_l_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '8390_l_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>8390р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>8390 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '10990_l_f':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>10990р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>10990 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5500_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '11000_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>11000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '16500_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>16500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>16500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '21900_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>21900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>21900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '1000_g_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>1000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>1000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_g_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5501_g_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5600р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5600 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '8390_g_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>8390р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>8390 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '10990_g_matstat':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>11990р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11990 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5500_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '11000_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>11000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '16500_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>16500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>16500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '21900_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>21900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>21900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '1000_g_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>1000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>1000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_g_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5501_g_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5600р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5600 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '8390_g_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>8390р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>8390 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '10990_g_mikra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>10990р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>10990 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5500_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '11000_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>1100р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '16500_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>16500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>16500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '21900_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>21900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>21900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '1000_g_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>1000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>1000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_g_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5501_g_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5600р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5600 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '8390_g_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>8390р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>8390 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '10990_g_makra':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>10990р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>10990 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должен быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5500_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '11000_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>11000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>11000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '16500_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>16500р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>16500 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '21900_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>21900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>21900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '1000_g_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>1000р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>1000 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '2900_g_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>2900р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>2900 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '5501_g_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>5600р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>5600 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '8390_g_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>8390р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>8390 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()

    elif callback.data == '10990_g_demo':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b> пришлите, пожалуйста '
                                    f'скриншот, '
                                    f'подтверждающий оплату. <b>Сумма перевода</b> должна составлять <b>10990р</b>.\n\n'
                                    f'<b>Правила отправления скриншота о переводе</b>:\n\n'
                                    f'<b>Дата</b> перевода должна быть <b>сегдняшней</b>, то есть'
                                    f' <b>{datetime.now().date()}</b>,\n\n'
                                    f'<b>Сумма перевода</b> не должна отличаться от указанной сверху, то есть'
                                    f' <b>10990 рублей</b>,\n\n'
                                    f'<b>Номер телефона</b>, по которому совершается перевод, должно быть'
                                    f' <b>+79017572093</b>\n\n'
                                    f'Сбербанк',
                               parse_mode="HTML")

        await callback.message.delete()


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def process_photo(message: types.Message):
    photo = message.photo[-1]
    photo_path = f"photo_{photo.file_id}.jpg"
    await photo.download(photo_path)
    result = reader.readtext(photo_path)
    list_from_text = ''
    text = "\n".join([i[1] for i in result])
    await bot.send_message(chat_id=683092826,
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

    if 3000 in num_list or '3000 ₽' in text or '3 ООО ₽' in text or '3000.00' in text or '3 000.00 p.' in text or \
            '3 000.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 3000 рублей\n')
        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>3000 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 3000 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 5).value is None and \
                worksheet.cell(row_number, column_number + 4).value is None:
            worksheet.update_cell(row_number, column_number + 4, 1)
            worksheet.update_cell(row_number, column_number + 5, 3000)
        else:
            amount = int(worksheet.cell(row_number, column_number + 4).value) + 1
            price = int(worksheet.cell(row_number, column_number + 5).value) + 3000
            worksheet.update_cell(row_number, column_number + 4, amount)
            worksheet.update_cell(row_number, column_number + 5, price)

    elif 2000 in num_list or '2000 ₽' in text or '2 ООО ₽' in text or '2000.00' in text or '2 000.00 p.' in text or \
            '2 000.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2000 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2000 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2000 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 5).value is None and \
                worksheet.cell(row_number, column_number + 4).value is None:
            worksheet.update_cell(row_number, column_number + 4, 1)
            worksheet.update_cell(row_number, column_number + 5, 2000)
        else:
            amount = int(worksheet.cell(row_number, column_number + 4).value) + 1
            price = int(worksheet.cell(row_number, column_number + 5).value) + 2000
            worksheet.update_cell(row_number, column_number + 4, amount)
            worksheet.update_cell(row_number, column_number + 5, price)

    elif 2000 in num_list or '2250 ₽' in text or '2 25О ₽' in text or '2250.00' in text or '2 250.00 p.' in text or \
            '2 250.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2250 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2250 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2250 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 5).value is None and \
                worksheet.cell(row_number, column_number + 4).value is None:
            worksheet.update_cell(row_number, column_number + 4, 1)
            worksheet.update_cell(row_number, column_number + 5, 2250)
        else:
            amount = int(worksheet.cell(row_number, column_number + 4).value) + 1
            price = int(worksheet.cell(row_number, column_number + 5).value) + 2250
            worksheet.update_cell(row_number, column_number + 4, amount)
            worksheet.update_cell(row_number, column_number + 5, price)

    elif 2000 in num_list or '2750 ₽' in text or '2 75О ₽' in text or '2750.00' in text or '2 750.00 p.' in text or \
            '2 750.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2750 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2750 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2750 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 5).value is None and \
                worksheet.cell(row_number, column_number + 4).value is None:
            worksheet.update_cell(row_number, column_number + 4, 1)
            worksheet.update_cell(row_number, column_number + 5, 2750)
        else:
            amount = int(worksheet.cell(row_number, column_number + 4).value) + 1
            price = int(worksheet.cell(row_number, column_number + 5).value) + 2750
            worksheet.update_cell(row_number, column_number + 4, amount)
            worksheet.update_cell(row_number, column_number + 5, price)

    elif 2500 in num_list or '2500 ₽' in text or '2 5ОО ₽' in text or '2500.00' in text or '2 500.00 p.' in text or \
            '2 500.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2500 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2500 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2500 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 5).value is None and \
                worksheet.cell(row_number, column_number + 4).value is None:
            worksheet.update_cell(row_number, column_number + 4, 1)
            worksheet.update_cell(row_number, column_number + 5, 2500)
        else:
            amount = int(worksheet.cell(row_number, column_number + 4).value) + 1
            price = int(worksheet.cell(row_number, column_number + 5).value) + 2500
            worksheet.update_cell(row_number, column_number + 4, amount)
            worksheet.update_cell(row_number, column_number + 5, price)

    elif 2400 in num_list or '2400 ₽' in text or '2 4ОО ₽' in text or '2400.00' in text or '2 400.00 p.' in text or \
            '2 400.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы совершили покупку.\n'
                                    f'Сумма покупки составила 2400 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2400 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2400 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 5).value is None and \
                worksheet.cell(row_number, column_number + 4).value is None:
            worksheet.update_cell(row_number, column_number + 4, 1)
            worksheet.update_cell(row_number, column_number + 5, 2400)
        else:
            amount = int(worksheet.cell(row_number, column_number + 4).value) + 1
            price = int(worksheet.cell(row_number, column_number + 5).value) + 2400
            worksheet.update_cell(row_number, column_number + 4, amount)
            worksheet.update_cell(row_number, column_number + 5, price)

    elif 1000 in num_list or '1000 ₽' in text or '1 0ОО ₽' in text or '1000.00' in text or '1 000.00 p.' in text or \
            '1 000.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели групповой курс.\n'
                                    f'Сумма покупки составила 1000 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>1000 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 1000 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку одного группового занятия.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>1000 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 7).value is None:
            worksheet.update_cell(row_number, column_number + 7, 1000)
        else:
            amount = int(worksheet.cell(row_number, column_number + 7).value) + 1000
            worksheet.update_cell(row_number, column_number + 7, amount)

    elif 2100 in num_list or '2100 ₽' in text or '2 1ОО ₽' in text or '2100.00' in text or '2 100.00 p.' in text or \
            '2 100.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели индивидульный курс.\n'
                                    f'Сумма покупки составила 2100 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2100 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2100 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку одного индивидуального '
                                     f'занятия.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2100 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 6).value is None:
            worksheet.update_cell(row_number, column_number + 6, 2900)
        else:
            amount = int(worksheet.cell(row_number, column_number + 6).value) + 2900
            worksheet.update_cell(row_number, column_number + 6, amount)

    elif 5500 in num_list or '5500 ₽' in text or '5 5ОО ₽' in text or '5500.00' in text or '5 500.00 p.' in text or \
            '5 500.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели индивидульный курс.\n'
                                    f'Сумма покупки составила 5500 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>5500 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 5500 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку шести групповых занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>5500 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 6).value is None:
            worksheet.update_cell(row_number, column_number + 6, 5500)
        else:
            amount = int(worksheet.cell(row_number, column_number + 6).value) + 5500
            worksheet.update_cell(row_number, column_number + 6, amount)

    elif 11000 in num_list or '11000 ₽' in text or '11 0ОО ₽' in text or '11000.00' in text or '11 000.00 p.' in text \
            or '11 000.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели индивидуальный курс.\n'
                                    f'Сумма покупки составила 11000 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>11000 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 11000 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку шести индивидуальных '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>5500 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 6).value is None:
            worksheet.update_cell(row_number, column_number + 6, 11000)
        else:
            amount = int(worksheet.cell(row_number, column_number + 6).value) + 11000
            worksheet.update_cell(row_number, column_number + 6, amount)

    elif 16500 in num_list or '16500 ₽' in text or '16 5ОО ₽' in text or '16500.00' in text or '16 500.00 p.' in text \
            or '16 500.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели индивидуальный курс.\n'
                                    f'Сумма покупки составила 16500 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>16500 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 16500 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку девяти индивидуальных '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>16500 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 6).value is None:
            worksheet.update_cell(row_number, column_number + 6, 16500)
        else:
            amount = int(worksheet.cell(row_number, column_number + 6).value) + 16500
            worksheet.update_cell(row_number, column_number + 6, amount)

    elif 219000 in num_list or '21900 ₽' in text or '21 9ОО ₽' in text or '21900.00' in text or '21 900.00 p.' in text \
            or '21 900.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели индивидуальный курс.\n'
                                    f'Сумма покупки составила 21900 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>21900 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 21900 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку двеннадцати индивидуальных '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>21900 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 6).value is None:
            worksheet.update_cell(row_number, column_number + 6, 21900)
        else:
            amount = int(worksheet.cell(row_number, column_number + 6).value) + 21900
            worksheet.update_cell(row_number, column_number + 6, amount)

    elif 2900 in num_list or '2900 ₽' in text or '2 9ОО ₽' in text or '2900.00' in text or '2 900.00 p.' in text \
            or '2 900.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели групповой курс.\n'
                                    f'Сумма покупки составила 2900 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2900 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 2900 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку трех групповых '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>2900 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 7).value is None:
            worksheet.update_cell(row_number, column_number + 7, 2900)
        else:
            amount = int(worksheet.cell(row_number, column_number + 7).value) + 2900
            worksheet.update_cell(row_number, column_number + 7, amount)

    elif 5600 in num_list or '5600 ₽' in text or '5 6ОО ₽' in text or '5600.00' in text or '5 600.00 p.' in text \
            or '5 600.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели групповый курс.\n'
                                    f'Сумма покупки составила 5600 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>5600 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 5600 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку шести групповых '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>5600 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 7).value is None:
            worksheet.update_cell(row_number, column_number + 7, 5600)
        else:
            amount = int(worksheet.cell(row_number, column_number + 7).value) + 5600
            worksheet.update_cell(row_number, column_number + 7, amount)

    elif 8390 in num_list or '8390 ₽' in text or '8 39О ₽' in text or '8390.00' in text or '8 390.00 p.' in text \
            or '8 390.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели групповой курс.\n'
                                    f'Сумма покупки составила 8390 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>8390 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 8390 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку девяти групповых '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>8390 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 7).value is None:
            worksheet.update_cell(row_number, column_number + 7, 8390)
        else:
            amount = int(worksheet.cell(row_number, column_number + 7).value) + 8390
            worksheet.update_cell(row_number, column_number + 7, amount)

    elif 10990 in num_list or '10990 ₽' in text or '10 99О ₽' in text or '10990.00' in text or '10 990.00 p.' in text \
            or '10 990.00 p' in text:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, вы приобрели групповой курс.\n'
                                    f'Сумма покупки составила 10990 рублей\n')

        await bot.send_photo(chat_id=5490940595,
                             caption=f'Уважаемый Даниилл, пользователь совершил покупку в вашем боте.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>10990 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, пользователь совершил покупку в телеграм боте. '
                                     f'Вот его данные:\n\n'
                                     f'Ник в Телеграме: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Cумма покупки 10990 рублей\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

        await bot.send_photo(chat_id=317434662,
                             caption=f'Уважаемый Максимилиан, пользователь совершил покупку двеннадцати групповых '
                                     f'занятий.\n'
                                     f'Данные пользователя:\n'
                                     f'Ник в телеграме: <b>{message.from_user.full_name}</b>\n'
                                     f'Дата совершения покупки: <b>{datetime.now().date()}</b>'
                                     f'Сумма покупки составила <b>10990 рублей</b>',
                             parse_mode='HTML',
                             photo=message.photo[-1].file_id)

        cell = worksheet.find(str(message.from_user.id))
        row_number = cell.row
        column_number = cell.col
        if worksheet.cell(row_number, column_number + 7).value is None:
            worksheet.update_cell(row_number, column_number + 7, 10990)
        else:
            amount = int(worksheet.cell(row_number, column_number + 7).value) + 10990
            worksheet.update_cell(row_number, column_number + 7, amount)

    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, ваша заявка находится на '
                                    f'рассмотрении.\n'
                                    f'Ожидайте ответа от технической поддержки.')
        await bot.send_photo(chat_id=683092826,
                             caption=f'Дмитрий Михайлович, произошла ошибка во время оплаты: невозможно проверить'
                                     f'действительность оплаты.\n\n'
                                     f'Данные о пользователе:\n\n'
                                     f'Ник в Телеграм: {message.from_user.full_name}\n'
                                     f'Дата покупки: {datetime.now().date()}\n'
                                     f'Скриншот оплаты представлен сверху',
                             photo=message.photo[-1].file_id)

    os.remove(photo_path)

if __name__ == "__main__":
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)

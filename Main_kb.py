from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
Raspisanie = KeyboardButton('Помощь в учебе')
Prepodi = KeyboardButton('🍾Nondum Party')
Kafedri = KeyboardButton('Заказы одежды с Poizon')
kb_main.add(Raspisanie).insert(Prepodi).add(Kafedri)

tusovki_kb = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Наше сообщество',
                            url='https://vk.com/nondum.party')
btn2 = InlineKeyboardButton(text='Ближайшие мероприятия',
                            callback_data='parties')
btn3 = InlineKeyboardButton(text='Покупка билета',
                            callback_data='buy')
tusovki_kb.add(btn1).add(btn2).add(btn3)

poison_kb = InlineKeyboardMarkup(row_width=1)
poison_btn = InlineKeyboardButton(text='За покупками',
                                  url='https://t.me/nondumclothes')
poison_kb.add(poison_btn)

studying_main_btns = [
    InlineKeyboardButton(text='Первый курс', callback_data='first_course'),
    InlineKeyboardButton(text='Второй курс', callback_data='second_course'),
]
studying_main_kb = InlineKeyboardMarkup().row(*studying_main_btns)

studying_first_btns = [
    InlineKeyboardButton(text='Материалы', callback_data='files_first_course'),
    InlineKeyboardButton(text='Занятия', callback_data='lessons_first_course'),
]
studying_first_kb = InlineKeyboardMarkup().row(*studying_first_btns)

studying_second_btns = [
    InlineKeyboardButton(text='Материалы', callback_data='files_second_course'),
    InlineKeyboardButton(text='Занятия', callback_data='lessons_second_course'),
]
studying_second_kb = InlineKeyboardMarkup().row(*studying_second_btns)

subjects_first_btns = [
    InlineKeyboardButton(text='Матан', callback_data='matan_first_s'),
    InlineKeyboardButton(text='Линал', callback_data='linal_first_s'),
    InlineKeyboardButton(text='ЭкГео', callback_data='ekgeo_first_s'),
    InlineKeyboardButton(text='Ввэк', callback_data='vvek_first_s')

]
subjects_first_kb = InlineKeyboardMarkup().row(*subjects_first_btns)

lessons_first_btns = [
    InlineKeyboardButton(text='Матан', callback_data='matan_first'),
    InlineKeyboardButton(text='Линал', callback_data='linal_first'),

]
lessons_first_kb = InlineKeyboardMarkup().row(*lessons_first_btns)

subjects_second_btns = [
    InlineKeyboardButton(text='Матстат', callback_data='matstat_s'),
    InlineKeyboardButton(text='Микра', callback_data='mikra_s'),
    InlineKeyboardButton(text='Макра', callback_data='makra_s'),
    InlineKeyboardButton(text='Демография', callback_data='demograf_s')

]
subjects_second_kb = InlineKeyboardMarkup().row(*subjects_second_btns)

lessons_second_btns = [
    InlineKeyboardButton(text='Матстат', callback_data='matstat'),
    InlineKeyboardButton(text='Микра', callback_data='mikra'),
    InlineKeyboardButton(text='Макра', callback_data='makra'),
    InlineKeyboardButton(text='Демография', callback_data='demograf')

]
lessons_second_kb = InlineKeyboardMarkup().row(*lessons_second_btns)

types_of_lessons_first_matan_btns = [
    InlineKeyboardButton(text='Индивидуально', callback_data='individual_first_m'),
    InlineKeyboardButton(text='В группе', callback_data='group_first_m'),

]
types_of_lessons_first_matan_kb = InlineKeyboardMarkup().row(*types_of_lessons_first_matan_btns)

types_of_lessons_first_linal_btns = [
    InlineKeyboardButton(text='Индивидуально', callback_data='individual_first_l'),
    InlineKeyboardButton(text='В группе', callback_data='group_first_l'),

]
types_of_lessons_first_linal_kb = InlineKeyboardMarkup().row(*types_of_lessons_first_linal_btns)

types_of_individual_lessons_first_matan_btns = [
    InlineKeyboardButton(text='5500', callback_data='5500_f_m'),
    InlineKeyboardButton(text='11000', callback_data='11000_f_m'),
    InlineKeyboardButton(text='16500', callback_data='16500_f_m'),
    InlineKeyboardButton(text='21900', callback_data='21900_f_m'),

]
types_of_individual_lessons_first_matan_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_first_matan_btns)

types_of_individual_lessons_first_linal_btns = [
    InlineKeyboardButton(text='5500', callback_data='5500_f_l'),
    InlineKeyboardButton(text='11000', callback_data='11000_f_l'),
    InlineKeyboardButton(text='16500', callback_data='16500_f_l'),
    InlineKeyboardButton(text='21900', callback_data='21900_f_l'),

]
types_of_individual_lessons_first_linal_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_first_linal_btns)

types_of_group_lessons_first_matan_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_f_m'),
    InlineKeyboardButton(text='5500', callback_data='5501_f_m'),
    InlineKeyboardButton(text='8390', callback_data='8390_f_m'),
    InlineKeyboardButton(text='10990', callback_data='10990_f_m'),

]
types_of_group_lessons_first_matan_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_first_matan_btns)

types_of_group_lessons_first_linal_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_l_m'),
    InlineKeyboardButton(text='5500', callback_data='5501_l_m'),
    InlineKeyboardButton(text='8390', callback_data='8390_l_m'),
    InlineKeyboardButton(text='10990', callback_data='10990_l_m'),

]
types_of_group_lessons_first_linal_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_first_linal_btns)



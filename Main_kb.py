from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
Raspisanie = KeyboardButton('Помощь в учебе')
Prepodi = KeyboardButton('🍾Nondum Party')
Kafedri = KeyboardButton('Заказы одежды с Poizon')
kb_main.add(Raspisanie).insert(Prepodi).add(Kafedri)

tusovki_kb = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Наше сообщество',
                            url='https://vk.com/nondum.party')
btn2 = InlineKeyboardButton(text='Ближайшее мероприятие',
                            callback_data='parties')
btn3 = InlineKeyboardButton(text='Купить билет',
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


lessons_second_btns = [
    InlineKeyboardButton(text='Матстат', callback_data='matstat'),
    InlineKeyboardButton(text='Микра', callback_data='mikra'),
    InlineKeyboardButton(text='Макра', callback_data='makra'),
    InlineKeyboardButton(text='Демография', callback_data='demograf')

]
lessons_second_kb = InlineKeyboardMarkup().row(*lessons_second_btns[:3]).add(lessons_second_btns[3])

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
    InlineKeyboardButton(text='2900', callback_data='2900_f_m'),
    InlineKeyboardButton(text='5500', callback_data='5500_f_m'),
    InlineKeyboardButton(text='11000', callback_data='11000_f_m'),
    InlineKeyboardButton(text='16500', callback_data='16500_f_m'),
    InlineKeyboardButton(text='21900', callback_data='21900_f_m'),

]
types_of_individual_lessons_first_matan_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_first_matan_btns[:4]).add(types_of_individual_lessons_first_matan_btns[4])

types_of_individual_lessons_first_linal_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_f_l'),
    InlineKeyboardButton(text='5500', callback_data='5500_f_l'),
    InlineKeyboardButton(text='11000', callback_data='11000_f_l'),
    InlineKeyboardButton(text='16500', callback_data='16500_f_l'),
    InlineKeyboardButton(text='21900', callback_data='21900_f_l'),

]
types_of_individual_lessons_first_linal_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_first_linal_btns[:4]).add(types_of_individual_lessons_first_linal_btns[4])

types_of_group_lessons_first_matan_btns = [
    InlineKeyboardButton(text='1000', callback_data='1000_m_f'),
    InlineKeyboardButton(text='2900', callback_data='2900_m_f'),
    InlineKeyboardButton(text='5600', callback_data='5501_m_f'),
    InlineKeyboardButton(text='8390', callback_data='8390_m_f'),
    InlineKeyboardButton(text='10990', callback_data='10990_m_f'),

]
types_of_group_lessons_first_matan_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_first_matan_btns[:4]).add(types_of_group_lessons_first_matan_btns[4])

types_of_group_lessons_first_linal_btns = [
    InlineKeyboardButton(text='1000', callback_data='1000_l_f'),
    InlineKeyboardButton(text='2900', callback_data='2900_l_f'),
    InlineKeyboardButton(text='5600', callback_data='5501_l_f'),
    InlineKeyboardButton(text='8390', callback_data='8390_l_f'),
    InlineKeyboardButton(text='10990', callback_data='10990_l_f'),

]
types_of_group_lessons_first_linal_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_first_linal_btns).add(types_of_group_lessons_first_linal_btns[4])

return_to_buy_ticket = [
    InlineKeyboardButton(text='Купить билет', callback_data='buy')
]
buy_ticket_kb = InlineKeyboardMarkup().row(*return_to_buy_ticket)

types_of_lessons_second_matstat_btns = [
    InlineKeyboardButton(text='Индивидуально', callback_data='individual_matstat'),
    InlineKeyboardButton(text='В группе', callback_data='group_matstat'),

]
types_of_lessons_second_matstat_kb = InlineKeyboardMarkup().row(*types_of_lessons_second_matstat_btns)

types_of_lessons_second_mikra_btns = [
    InlineKeyboardButton(text='Индивидуально', callback_data='individual_mikra'),
    InlineKeyboardButton(text='В группе', callback_data='group_mikra'),

]
types_of_lessons_second_mikra_kb = InlineKeyboardMarkup().row(*types_of_lessons_second_mikra_btns)

types_of_lessons_second_makra_btns = [
    InlineKeyboardButton(text='Индивидуально', callback_data='individual_makra'),
    InlineKeyboardButton(text='В группе', callback_data='group_makra'),

]
types_of_lessons_second_makra_kb = InlineKeyboardMarkup().row(*types_of_lessons_second_makra_btns)

types_of_lessons_second_demo_btns = [
    InlineKeyboardButton(text='Индивидуально', callback_data='individual_demo'),
    InlineKeyboardButton(text='В группе', callback_data='group_demo'),

]
types_of_lessons_second_demo_kb = InlineKeyboardMarkup().row(*types_of_lessons_second_demo_btns)

types_of_individual_lessons_second_matstat_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_matstat'),
    InlineKeyboardButton(text='5500', callback_data='5500_matstat'),
    InlineKeyboardButton(text='11000', callback_data='11000_matstat'),
    InlineKeyboardButton(text='16500', callback_data='16500_matstat'),
    InlineKeyboardButton(text='21900', callback_data='21900_matstat'),

]
types_of_individual_lessons_second_matstat_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_second_matstat_btns[:4]).add(types_of_individual_lessons_second_matstat_btns[4])

types_of_group_lessons_second_matstat_btns = [
    InlineKeyboardButton(text='1000', callback_data='1000_g_matstat'),
    InlineKeyboardButton(text='2900', callback_data='2900_g_matstat'),
    InlineKeyboardButton(text='5600', callback_data='5501_g_matstat'),
    InlineKeyboardButton(text='8390', callback_data='8390_g_matstat'),
    InlineKeyboardButton(text='10990', callback_data='10990_g_matstat'),

]
types_of_group_lessons_second_matstat_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_second_matstat_btns[:4]).add(types_of_group_lessons_second_matstat_btns[4])

types_of_individual_lessons_second_mikra_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_mikra'),
    InlineKeyboardButton(text='5500', callback_data='5500_mikra'),
    InlineKeyboardButton(text='11000', callback_data='11000_mikra'),
    InlineKeyboardButton(text='16500', callback_data='16500_mikra'),
    InlineKeyboardButton(text='21900', callback_data='21900_mikra'),

]
types_of_individual_lessons_second_mikra_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_second_mikra_btns[:4]).add(types_of_individual_lessons_second_mikra_btns[4])

types_of_group_lessons_second_mikra_btns = [
    InlineKeyboardButton(text='1000', callback_data='1000_g_mikra'),
    InlineKeyboardButton(text='2900', callback_data='2900_g_mikra'),
    InlineKeyboardButton(text='5600', callback_data='5501_g_mikra'),
    InlineKeyboardButton(text='8390', callback_data='8390_g_mikra'),
    InlineKeyboardButton(text='10990', callback_data='10990_g_mikra'),

]
types_of_group_lessons_second_mikra_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_second_mikra_btns[:4]).add(types_of_group_lessons_second_mikra_btns[4])

types_of_individual_lessons_second_makra_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_makra'),
    InlineKeyboardButton(text='5500', callback_data='5500_makra'),
    InlineKeyboardButton(text='11000', callback_data='11000_makra'),
    InlineKeyboardButton(text='16500', callback_data='16500_makra'),
    InlineKeyboardButton(text='21900', callback_data='21900_makra'),

]
types_of_individual_lessons_second_makra_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_second_makra_btns[:4]).add(types_of_individual_lessons_second_makra_btns[4])

types_of_group_lessons_second_makra_btns = [
    InlineKeyboardButton(text='1000', callback_data='1000_g_makra'),
    InlineKeyboardButton(text='2900', callback_data='2900_g_makra'),
    InlineKeyboardButton(text='5600', callback_data='5501_g_makra'),
    InlineKeyboardButton(text='8390', callback_data='8390_g_makra'),
    InlineKeyboardButton(text='10990', callback_data='10990_g_makra'),

]
types_of_group_lessons_second_makra_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_second_makra_btns[:4]).add(types_of_group_lessons_second_makra_btns[4])

types_of_individual_lessons_second_demo_btns = [
    InlineKeyboardButton(text='2900', callback_data='2900_demo'),
    InlineKeyboardButton(text='5500', callback_data='5500_demo'),
    InlineKeyboardButton(text='11000', callback_data='11000_demo'),
    InlineKeyboardButton(text='16500', callback_data='16500_demo'),
    InlineKeyboardButton(text='21900', callback_data='21900_demo'),

]
types_of_individual_lessons_second_demo_kb = InlineKeyboardMarkup().row(*types_of_individual_lessons_second_demo_btns[:4]).add(types_of_individual_lessons_second_demo_btns[4])

types_of_group_lessons_second_demo_btns = [
    InlineKeyboardButton(text='1000', callback_data='1000_g_demo'),
    InlineKeyboardButton(text='2900', callback_data='2900_g_demo'),
    InlineKeyboardButton(text='5600', callback_data='5501_g_demo'),
    InlineKeyboardButton(text='8390', callback_data='8390_g_demo'),
    InlineKeyboardButton(text='10990', callback_data='10990_g_demo'),

]
types_of_group_lessons_second_demo_kb = InlineKeyboardMarkup().row(*types_of_group_lessons_second_demo_btns).add(types_of_group_lessons_second_demo_btns[4])
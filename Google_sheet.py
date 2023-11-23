import gspread

gc = gspread.service_account(filename='nondumbot-912fdd73a98c.json')
sh = gc.open("NonDumBOT")
worksheet = sh.sheet1
worksheet.update_cell(1, 1, 'id пользователя')
worksheet.update_cell(1, 2, 'Telegram никнейм')
worksheet.update_cell(1, 3, 'Роль пользователя')
worksheet.update_cell(1, 4, 'Дата авторизации')
worksheet.update_cell(1, 5, 'Количество купленных билетов')
worksheet.update_cell(1, 6, 'Общая сумма, уплаченная за билеты')
worksheet.update_cell(1, 7, 'Оплата индивидуальных занятий')
worksheet.update_cell(1, 8, 'Оплата групповых занятий')


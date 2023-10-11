import gspread

gc = gspread.service_account(filename='nondumbot-912fdd73a98c.json')
sh = gc.open("NonDumBOT")
worksheet = sh.sheet1
worksheet.update_cell(1, 1, 'id клиента')
worksheet.update_cell(1, 2, 'Telegram nickname')
worksheet.update_cell(1, 3, 'Роль пользователя')
worksheet.update_cell(1, 4, 'Дата и время авторизации')
worksheet.update_cell(1, 5, 'Куплен ли билет?')
worksheet.update_cell(1, 6, 'Цена, уплаченная за билет')
worksheet.update_cell(1, 7, 'Был ли возврат билета?')
worksheet.update_cell(1, 8, 'Сумма покупок на Poizon')


from openpyxl import Workbook
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
wb.save("Nondum_clients.xlsx")
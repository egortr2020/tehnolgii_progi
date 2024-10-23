import telebot
from telebot import types
import openpyxl
bot = telebot.TeleBot('7706917053:AAH3A9HM3Do7ul0SPnmiQKCEYOvgNy3ia3U')

workbook = openpyxl.load_workbook("24-knt.xlsx")
sheet = workbook.active

day_ranges = {
    "понедельник": (12, 19),
    "вторник": (23, 30),
    "среда": (34, 41),
    "четверг": (51, 52),
    "пятница": (56, 63),
    "суббота": (67, 74)
}

group_columns = {
    "кнт-1": [3, 5, 6],
    "кнт-2": [3, 8, 9],
    "кнт-3": [3, 11, 12],
    "кнт-4": [3, 17, 18],
    "кнт-5": [3, 20, 21],
    "кнт-6": [3, 23, 24],
    "кнт-7": [3, 29, 30],
    "кнт-8": [3, 32, 33],
    "кнт-9": [3, 35, 36]
}

day_input = input("Введите день недели (понедельник-суббота): ").lower()
group_input = input("Введите группу (кнт-1 - кнт-9): ").lower()

if day_input in day_ranges and group_input in group_columns:
    start_row, end_row = day_ranges[day_input]
    selected_columns = group_columns[group_input]

    gg = ""
    for row_num in range(start_row, end_row + 1):
        empty_row = False
        for col_num in selected_columns: 
            cell = sheet.cell(row=row_num, column=col_num)
            if cell.value is None:
                empty_row = True
                break

        if not empty_row:
            for col_num in selected_columns:
                cell = sheet.cell(row=row_num, column=col_num)
                gg += str(cell.value) + " "
            gg += "\n"

    print(gg)

else:
    print("Неверный день недели или группа.")
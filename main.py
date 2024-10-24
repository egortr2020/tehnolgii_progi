import telebot
from telebot import types
import openpyxl
bot = telebot.TeleBot('7655400381:AAFIYnMA_7HKJJoi7ight0gwsthjVlj630s')

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

"""if day_input in day_ranges and group_input in group_columns:
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
    print("Неверный день недели или группа.")"""
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('24-кнт', callback_data='24-кнт'))
    bot.reply_to(message, 'Привет, Выбери свой поток!', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    global selected_group
    if callback.data == '24-кнт':
        markup = types.InlineKeyboardMarkup()
        for group_name in group_columns:
            markup.add(types.InlineKeyboardButton(group_name.upper(), callback_data=group_name))
        bot.send_message(callback.message.chat.id, 'Выбери группу:', reply_markup=markup)
    
    
    
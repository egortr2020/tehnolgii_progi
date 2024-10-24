import telebot
from telebot import types
import openpyxl
import pickle

bot = telebot.TeleBot('7655400381:AAFIYnMA_7HKJJoi7ight0gwsthjVlj630s')
users = {}
workbook = openpyxl.load_workbook("24-knt.xlsx")
sheet = workbook.active
YANDEX_DISK_URL = "https://disk.yandex.ru/i/yB5rVDGydfOy6A"
LOCAL_FILE_NAME = "24-knt.xlsx"
NEW_FILE_NAME = "24-knt_obnova.xlsx"

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

selected_group = None
def load_users():
    global users
    try:
        with open('users.pkl', 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        users = {}


def save_users():
    global users
    with open('users.pkl', 'wb') as f:
        pickle.dump(users, f)


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
    elif callback.data in group_columns:
        selected_group = callback.data
        markup = types.InlineKeyboardMarkup()
        for day_name in day_ranges:
            markup.add(types.InlineKeyboardButton(day_name.capitalize(), callback_data=day_name))
        bot.send_message(callback.message.chat.id, 'Выбери день недели:', reply_markup=markup)

    elif callback.data in day_ranges and selected_group is not None:
        start_row, end_row = day_ranges[callback.data]
        selected_columns = group_columns[selected_group]

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

        bot.send_message(callback.message.chat.id, gg)


bot.polling(non_stop=True)

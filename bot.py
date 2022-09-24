import telebot
from telebot import types


token = "5529319076:AAGNH5OQPmq7ZHXoGOaiDFbP-gnwb6qyJwY"
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_yes = types.InlineKeyboardButton(text="Да", callback_data="Yes")
    keyboard_no = types.InlineKeyboardButton(text="Нет", callback_data="No")
    keyboard.add(keyboard_yes, keyboard_no)
    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    markup = create_keyboard()
    bot.send_message(message.chat.id, "Привет, я бот-помощник, помогу тебе выбрать восстановленный недорогой телефон")
    bot.send_message(message.chat.id, " Тебе это интересно?", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_inline(callback):
    if callback.data == "Yes":
        pass
    elif callback.data == "No":
        bot.send_message(
            chat_id=callback.message.chat.id,
            text="Тогда ничем не могу тебе помочь. Пока")


bot.polling(none_stop=True)

import telebot
from telebot import types


token = "5529319076:AAGNH5OQPmq7ZHXoGOaiDFbP-gnwb6qyJwY"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот-помощник, помогу тебе выбрать восстановленный недорогой телефон")
    kb = types.InlineKeyboardMarkup()
    kb_yes = types.InlineKeyboardButton(text="Да", callback_data="Yes")
    kb_no = types.InlineKeyboardButton(text="Нет", callback_data="No")
    kb.add(kb_yes, kb_no)
    bot.send_message(message.chat.id, " Тебе это интересно?", reply_markup=kb)


bot.polling(none_stop=True)

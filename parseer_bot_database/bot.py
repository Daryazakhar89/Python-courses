import telebot
from telebot import types
from parser_mts import start_parsing, get_phones


token = "5529319076:AAGNH5OQPmq7ZHXoGOaiDFbP-gnwb6qyJwY"
bot = telebot.TeleBot(token)
BUTTONS = {
    "choose_phone_yes": types.InlineKeyboardButton(text="Yes", callback_data="Yes"),
    "choose_phone_no": types.InlineKeyboardButton(text="No", callback_data="No"),
    "parse_site": types.InlineKeyboardButton(text="Parse site", callback_data="parse_site"),
    "get_phones_from_db": types.InlineKeyboardButton(text="Get phones", callback_data="get_phones"),
}

keyboard = types.InlineKeyboardMarkup()


def get_phone_buttons(phones):
    return [types.InlineKeyboardButton(text=phone[0], callback_data=str(index)) for index, phone in enumerate(phones)]


def show_buttons_keyboard(buttons_to_show):
    keyboard.keyboard = []
    keyboard.add(*buttons_to_show)

    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello, I'm a helper bot, I'll help you choose a restored inexpensive phone")
    bot.send_message(message.chat.id, " Are you interested in it?", reply_markup=show_buttons_keyboard([
        BUTTONS["choose_phone_yes"],
        BUTTONS["choose_phone_no"]
    ]))


phones = []


@bot.callback_query_handler(func=lambda callback: True)
def callback_inline(callback):
    global phones
    if callback.data == "Yes":
        bot.send_message(
            chat_id=callback.message.chat.id,
            text="Please choose one of the following actions",
            reply_markup=show_buttons_keyboard([
                BUTTONS["parse_site"],
                BUTTONS["get_phones_from_db"]
            ])
        )
    elif callback.data == "No":
        bot.send_message(
            chat_id=callback.message.chat.id,
            text="Then I can't help you. Bye")
    elif callback.data == "parse_site":
        bot.send_message(
            chat_id=callback.message.chat.id,
            text="Wait for a moment while the site is parsing")
        start_parsing()
        bot.send_message(
            chat_id=callback.message.chat.id,
            text="Parsing has been finished",
            reply_markup=show_buttons_keyboard([
                BUTTONS["get_phones_from_db"]
            ])
        )
    elif callback.data == "get_phones":
        phones = get_phones()
        bot.send_message(
            chat_id=callback.message.chat.id,
            text="Parsing has been finished",
            reply_markup=show_buttons_keyboard(get_phone_buttons(phones))
        )
    else:
        index = int(callback.data)
        bot.send_message(
            chat_id=callback.message.chat.id,
            text=f"Model: {phones[index][0]}, Price: {phones[index][1]}"
        )


bot.polling(none_stop=True)

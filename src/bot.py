import telebot
from config import BOT_TOKEN, ADMINS_USERNAME, VALID_CHATS
from constants import WELCOME_MESSAGE
from llm import call_llm
from db import DBHandler


bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
db_handler = DBHandler()


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, WELCOME_MESSAGE)


def is_valid_admin_reply(message):
    is_admin = message.user.username in ADMINS_USERNAME
    is_valid_chat = message.chat.username in VALID_CHATS
    return is_admin and is_valid_chat


@bot.message_handler(func=lambda message: True)
def store_message(message):
    json_data = message.json
    db_handler.store_message(json_data)
    print(f"Stored message withDB: {json_data.get('message_id')}")


@bot.message_reaction_handler(
    func=lambda message: message.new_reaction and is_valid_admin_reply(message)
)
def handle_reaction(message: telebot.types.Message):
    reaction = message.new_reaction[-1].emoji
    if reaction not in ["👍"]:
        return

    message_text = db_handler.get_message(message.message_id).get("text")
    message = bot.reply_to(message, f"... صبر کنید  ")
    response = call_llm(message_text)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=response)


if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    try:
        bot.infinity_polling(
            allowed_updates=["message", "message_reaction"], restart_on_change=True
        )
    finally:
        db_handler.close()

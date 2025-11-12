from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("7315030675:AAGOiLrc98-_t1r6tBHnoopXqksh6kHUpNI")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Salom! Flask orqali ishlayapman 😊")

# Flask serverni ishga tushirish
if __name__ == "__main__":
    app.run()

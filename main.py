import telebot
from dotenv import load_dotenv
import os
from telebot import types

load_dotenv()
telegram_api_key = os.getenv('TELEGRAM_API_KEY')

bot = telebot.TeleBot(telegram_api_key)

start_button = types.InlineKeyboardButton(text="Game Start", callback_data="game_start")

game_button = types.InlineKeyboardButton(text="Play Game", url="https://staging.d22pwyeqd6avec.amplifyapp.com/")

@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.chat.id, "Welcome to the game!",
                     reply_markup=types.InlineKeyboardMarkup().add(start_button))

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "game_start":
        
        bot.send_message(call.message.chat.id, "Click the button to play:",
                         reply_markup=types.InlineKeyboardMarkup().add(game_button))

bot.polling()

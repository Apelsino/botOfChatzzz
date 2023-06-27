#Задача: написать чат-бота рулетку для коннекта рандомных
# людей и пусть они переписываются и я могу видеть их переписки
# и переписываться с ними от любого имени

import telebot
from telebot import types
bot = telebot.TeleBot('6059118014:AAHKFxLsCFxoQ23o4EMiN_NPO_eRi20JTIE')
@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, 'aye')

bot.polling(none_stop=True)
import telebot

token = 6219498131:AAFJ7qClb7wk9aqXhoZrYHRzDjr6DheYRmw

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

# Пишем первую функцию, которая отвечает "Привет" на команду /start
# Все функции общения приложения с ТГ спрятаны в функции под @
@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет')

# Запускаем бота. Он будет работать до тех пор, пока работает ячейка (крутится значок слева).
# Остановим ячейку - остановится бот
bot.polling()
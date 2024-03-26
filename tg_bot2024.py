import telebot
import conf
import joblib
from telebot import types
import scipy


bot = telebot.TeleBot(conf.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     """Привет! Чтобы проверить твое сообщение на токсичность, напиши /toxic_detect.\nЕсли хочешь посмотреть на статистику токсичности с сайта woman.ru, напиши /statistic""")

    @bot.message_handler(commands=['toxic_detect'])
    def send_intro(message):
        bot.send_message(message.chat.id,
                         "Введи сообщение для анализа токсичности")

        @bot.message_handler(func=lambda m: True)
        def send_tox(message):
            clf2 = joblib.load("model.pkl")
            answer = int(clf2.predict([message.text])[0])
            if answer == 1:
                bot.send_message(message.chat.id,
                                    "Твое высказываение токсичное.\n Перейти в начало /start")
            else:
                bot.send_message(message.chat.id,
                                    'Твое сообщение совсем не токсичное.\n Перейти в начало /start')

    @bot.message_handler(commands=['statistic'])
    def repeat_all_messages(message):
        # создаем клавиатуру
        keyboard = types.InlineKeyboardMarkup()

        # добавляем на нее две кнопки
        button1 = types.InlineKeyboardButton(text="Отношения", callback_data="relat")
        button2 = types.InlineKeyboardButton(text="Психология", callback_data="psycho")
        button3 = types.InlineKeyboardButton(text="Здоровье", callback_data="health")
        button4 = types.InlineKeyboardButton(text="Дети", callback_data="kids")
        button5 = types.InlineKeyboardButton(text="Дом", callback_data="home")
        button6 = types.InlineKeyboardButton(text="Красота", callback_data="beauty")
        button7 = types.InlineKeyboardButton(text="Мода", callback_data="fashion")
        button8 = types.InlineKeyboardButton(text="Отдых (осторожно, здесь есть мат)", callback_data="rest")
        button9 = types.InlineKeyboardButton(text="Звезды", callback_data="stars")
        button10 = types.InlineKeyboardButton(text="Диаграммы", callback_data="diag")
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        keyboard.add(button5)
        keyboard.add(button6)
        keyboard.add(button7)
        keyboard.add(button8)
        keyboard.add(button9)
        keyboard.add(button10)
        bot.send_message(message.chat.id, "Нажми на кнопку!", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.message:
            if call.data == "relat":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Отношения")
                with open('relations.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "psycho":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Психология")
                with open('psycho.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "health":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Здоровье")
                with open('health.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "kids":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Дети")
                with open('kids.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "home":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Дом")
                with open('home.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "beauty":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Красота")
                with open('beauty.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "fashion":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Мода")
                with open('fashion.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "rest":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Отдых")
                with open('rest.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "stars":
                bot.send_message(call.message.chat.id, "Это облако слов для категории Звезды")
                with open('stars.png', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")
            if call.data == "diag":
                bot.send_message(call.message.chat.id, "Это диаграммы")
                with open('diagram.jpg', 'rb') as f:
                    photo = f.read()
                    bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, "Еще диаграмм? /statistic. В начало /start")


if __name__ == '__main__':
    bot.polling(none_stop=True)
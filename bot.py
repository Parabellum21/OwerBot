import config
import telebot
from telebot import types
import pogoda
import spech
import pprint
import time
import translite

bot = telebot.TeleBot(config.token)
# 214655633 Саня
# 444713641 сергій
# 884214175 вова
# 93059159 TATO
pp = pprint.PrettyPrinter(indent=4)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('привіт', 'документація')
keyboard1.row('', 'погода')


@bot.message_handler(commands=['start', 'консоль'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Це, покищо, весь мій функціонал', reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):

    # print(message)
    print(message.chat.id, message.chat.first_name, message.text)
    # документація
    if message.text.lower() == 'документація':
        bot.send_message(message.chat.id, 'Вітаю на проекті OwerBot. Цей бот служить для експерементування різних функцій телеграм бота. Думаю що проект буде і далі розвиватися. Версія бота "alfa 0.021". Удачі ☺  ')
    elif message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Привіт ' +
                         message.chat.first_name + ', вітаю на мому проекті!')
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'впишіть "Країну, Місто"')
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(
            "Передати свої годані", request_location=True)
        keyboard.row(button_geo)
        bot.send_message(
            message.chat.id, "Передайте свої геодані", reply_markup=keyboard)
    else:
        text_transl=translite.leng(message.text)
        fl = spech.get_spech(text_transl)
        bot.send_voice(message.chat.id, voice=open(fl, 'rb'))
        bot.send_message(message.chat.id,text_transl)

        
@bot.message_handler(content_types=['document', 'audio', 'voice'])
def repeat_all_messages2(message):
    print('Прийшов звук')
    bot.send_voice(message.chat.id, voice=open('hello.mp3', 'rb'))


@bot.message_handler(content_types=['location'])
def handle_location(message):
    x = message.location.latitude
    y = message.location.longitude

    pog = """Погода для вашого регіону наступна:
		Швидкість вітру: {wind_spped} м/с
		вдносна вологість: {wologist}
		температура: {temp} C
		температура: max {temp_max}C, min {temp_min}C
		хмарність: {hmarnist}""".format(**pogoda.getpogoda(x, y))
    print(pog)
    bot.send_message(message.chat.id, pog)


# 'location': {'latitude': 48.139944, 'longitude': 23.029174}


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            # logger.error(e)
            time.sleep(15)

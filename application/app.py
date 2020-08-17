import request_weather_api as external_api
from models import Temperature as temp_db
# import sensor as dht11
# import led
import json
import math
import datetime
from telegram.ext import Updater, CommandHandler


def start_bot(update, context):
  message_people = 'Olá {} me chamo o Kawaii Temperature.\n Envie o comando /commands para saber todos os commands que eu possuo.\n Esse é um projeto de Bloco da https://github.com/hi-hi-ray'.format(update.message.from_user.first_name)
  led.flashing_light()
  print(update.message.from_user.first_name)
  update.message.reply_text(message_people)


def command_list(update, context):
  message_people = 'Olá {}, \n Então os comandos que temos disponíveis são: \n /now - Traz a umidade e temperatura em tempo real. \n /history - Traz o Histórico de medição da semana. \n /windchill - Traz a sensação térmica'.format(update.message.from_user.first_name)
  led.flashing_light()
  print(update.message.from_user.first_name)
  update.message.reply_text(message_people)


def get_temperature_now(update, context):
  led.flashing_light()
  humidity, temperature, timestamp = dht11.read_dht11()
  creation = temp_db.create(
        sensor_humidity=int(humidity),
        sensor_temperature=int(temperature),
        timestamp=str(timestamp),
        type_of_request="now")
  if creation.timestamp is not None:
      print("Temperature added")
  else:
      print("Failed to add temperature")
  led.flashing_light()
  print(update.message.from_user.first_name)
  message_temp = 'Olá {}!\n  A umidade é {} e a temperatura é {}.'.format(update.message.from_user.first_name, humidity, temperature)
  led.flashing_light()
  update.message.reply_text(message_temp)


def get_wind_chill(update, context):
  api_response = external_api.request_api()
  led.flashing_light()
  print(update.message.from_user.first_name)
  humidity, temperature, timestamp = dht11.read_dht11()
  led.flashing_light()
  windchill_response = calculate_wind_chill(int(temperature), api_response['wind']['speed'])
  creation = temp_db.create(
        sensor_humidity=int(humidity),
        sensor_temperature=int(temperature),
        wind_chill=str(windchill_response),
        timestamp=str(timestamp),
        type_of_request="windchill")
  if creation.timestamp is not None:
      print("Temperature added")
  else:
      print("Failed to add temperature")
  led.flashing_light()
  message_temp = 'Oiee {}! \n A sensação térmica estimada de hoje é de aproximadamente {}°C'.format(update.message.from_user.first_name, windchill_response)
  led.flashing_light()
  update.message.reply_text(message_temp)


def calculate_wind_chill(temperature, wind):
  wc = 33 + ((10*math.sqrt(wind)) + 10.45 - wind) * ((temperature - 33) / 22)
  return round(wc, 2)


def get_week_history(update, context):
  # led.flashing_light()
  print(update.message.from_user.first_name)
  # message_temp = 'Olá a umidade é {} e a temperatura é {}.'.format(humidity, temperature)
  # led.flashing_light()
  calcule_median_temp_and_humity()
  update.message.reply_text(calcule_median_temp_and_humity())


def calcule_median_temp_and_humity():
  now = datetime.datetime.now()
  then = now - datetime.timedelta(days=7)
  query = temp_db.select().where(temp_db.timestamp.between(str(datetime.datetime.timestamp(now)), str(datetime.datetime.timestamp(then))))
  result = query.execute()
  print(result)
  jsono = json.loads(result)
  return jsono


def main():
    updater = Updater('', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_bot))
    dp.add_handler(CommandHandler('commands', command_list))
    # dp.add_handler(CommandHandler('now', get_temperature_now))
    # dp.add_handler(CommandHandler('windchill', get_wind_chill))
    dp.add_handler(CommandHandler('history', get_week_history))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
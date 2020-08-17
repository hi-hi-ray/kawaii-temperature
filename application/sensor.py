import Adafruit_DHT
import RPi.GPIO as GPIO
from datetime import datetime

def read_dht11():
  # Primeiro valor é o tipo de sensor e o segundo é o nome do GPIO 
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  timestamp = (datetime.now().timestamp())
  return humidity, temperature, timestamp
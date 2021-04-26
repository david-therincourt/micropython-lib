# Test on Adafruit HUZZAH32 – ESP32 Feather Board
import bme280
from machine import I2C, Pin

i2c = I2C(sda=Pin(23), scl=Pin(22))

sensor = bme280.BME280(i2c=i2c)
sensor.formated_values

print(sensor.pressure/100, "hPa")
print(sensor.temperature, "°C")
print(sensor.humidity, "%")

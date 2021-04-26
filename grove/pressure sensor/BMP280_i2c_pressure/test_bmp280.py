# Test on Adafruit HUZZAH32 – ESP32 Feather Board
from machine import I2C, Pin
from bmp280 import *

i2c = I2C(sda=Pin(23), scl=Pin(22))
bmp = BMP280(i2c, addr=0x77)

print(bmp.temperature, "°C")
print(bmp.pressure/100, "hPa")


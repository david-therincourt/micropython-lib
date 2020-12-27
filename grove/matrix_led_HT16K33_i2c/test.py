from machine import I2C, Pin
from ht16k33_matrix import Matrix8x8
from time import sleep

i2c = I2C(freq=400000, sda=Pin(23), scl=Pin(22))  # Feather ESP32

mat = Matrix8x8(i2c)

for j in range(0,8,2):
    for i in range(0,8,2):
        mat.pixel(i,j,1)
        mat.show()
        sleep(.5)
        mat.pixel(i,j,0)
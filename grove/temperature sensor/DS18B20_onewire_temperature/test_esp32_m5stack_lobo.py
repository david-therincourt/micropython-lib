# Micropython ESP32 LoBo

from machine import Pin, Onewire
from time import sleep_ms

ow = Onewire(26)
ds = Onewire.ds18x20(ow, 0)

for i in range(5):
    temp = ds.convert_read()
    print(temp)
    sleep_ms(1000)
    
ds.deinit()
ow.deinit()

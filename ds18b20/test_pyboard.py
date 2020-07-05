from pyb import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms

pinD1 = Pin("D5")
ds = DS18X20(OneWire(pinD1))

roms = ds.scan()
print('found probes:', roms)

ds.convert_temp()
temp = ds.read_temp(roms[0])
print(temp)

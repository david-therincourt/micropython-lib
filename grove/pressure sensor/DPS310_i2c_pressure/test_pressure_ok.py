from machine import I2C, Pin
from time import sleep_ms
import math

c0 = 220
c1 = -296
c00 = 78449
c10 = -48133
c01 = -2228
c11 = 1273
c20 = -7183
c21 = 43
c30 = -814

sea_level_pressure = 101325 # Default = 

def twos_complement(val, bits):
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val

i2c = I2C(freq=400000, sda=Pin(23), scl=Pin(22))  # Feather ESP32
add = 0x77

i2c.writeto_mem(add, 0x06, b'\x66')  # PRS_CFG = 0x66
i2c.writeto_mem(add, 0x07, b'\xE6')  # TMP_CFG = 0x66 (b7 = 1 Internal temp sensor)
i2c.writeto_mem(add, 0x09, b'\x0C')  # CFG_REG = 0x0C


i2c.writeto_mem(add, 0x08, b'\x07')  # MEAS_CFG = Continous pressure end temperature measurement
# Read temp

buf = i2c.readfrom_mem(add, 0x03, 3)
print('temp =', buf)
t_raw = (buf[0] << 16) | (buf[1] << 8) | buf[2]
t_raw = twos_complement(t_raw, 24)
print('t_raw =', t_raw)
t_raw_sc = t_raw/1040384
print('t_raw_sc =', t_raw_sc)
temp = c0*0.5 + c1*t_raw_sc
print('temp =', temp)

# Read pressure
#i2c.writeto_mem(add, 0x08, b'\x01')  # MEAS_CFG = MEAS_CTRL(3 bit)
buf = i2c.readfrom_mem(add, 0x00, 3)
print('buf =', buf)
p_raw = (buf[0] << 16) | (buf[1] << 8) | buf[2]
p_raw = twos_complement(p_raw, 24)
print('p_raw =', p_raw)
p_raw_sc = p_raw/1040384
print('p_raw_sc =', p_raw_sc)
pressure = c00 + p_raw_sc*(c10 + p_raw_sc*(c20 + p_raw_sc*c30)) + t_raw_sc*c01 + t_raw_sc*p_raw_sc*(c11 + p_raw_sc*c21)
print('pressure =', pressure)

altitude = 44330 * (1.0 - math.pow(pressure / sea_level_pressure, 0.1903))
print("altitude =", altitude)




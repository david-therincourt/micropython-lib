from machine import I2C, Pin
from time import sleep_ms

c0 = 220
c1 = -296
c00 = 78449
c10 = -48133
c01 = -2228
c11 = 1273
c20 = -7183
c21 = 43
c30 = -814

def twos_complement(val, bits):
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val

i2c = I2C(freq=400000, sda=Pin(23), scl=Pin(22))  # Feather ESP32
add = 0x77

i2c.writeto_mem(add, 0x06, b'\x66')  # PRS_CFG = 0x66
i2c.writeto_mem(add, 0x07, b'\xE6')  # TMP_CFG = 0xE6 (b7 = 1 externel temp sensor)
i2c.writeto_mem(add, 0x09, b'\x0C')  # CFG_REG = 0x0C

i2c.writeto_mem(add, 0x08, b'\x02')  # MEAS_CFG = 0x02
buf = i2c.readfrom_mem(add, 0x03, 3)

print('temp =', buf)
t_raw = (buf[0] << 16) | (buf[1] << 8) | buf[2]
t_raw = twos_complement(t_raw, 24)
print('t_raw =', t_raw)
t_raw_sc = t_raw/1040384
print('t_raw_sc =', t_raw_sc)
temp = 220/2.0 - 296*t_raw_sc
print('temp =', temp)
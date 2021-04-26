from machine import I2C, Pin

def twos_complement(val, bits):
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val

i2c = I2C(freq=400000, sda=Pin(23), scl=Pin(22))  # Feather ESP32
add = 0x77

#i2c.writeto_mem(add, 1, b'\xC2\x85')  # Read on A0

buf = i2c.readfrom_mem(add, 0x10, 18)
print(buf)

c0 = (buf[0] << 4) | ((buf[1] >> 4) & 0x0F)
c0 = twos_complement(c0, 12)
print('c0 =', c0)

c1 = ((buf[1] & 0x0F) << 8) | buf[2]
c1 = twos_complement(c1, 12)
print('c1 =', c1)

c00 = (buf[3] << 12) | (buf[4] << 4) | ((buf[5] >> 4) & 0x0F)
c00 = twos_complement(c00, 20)
print('c00 =', c00)

c10 = ((buf[5] & 0x0F) << 16) | (buf[6] << 8) | buf[7]
c10 = twos_complement(c10, 20)
print('c10 =', c10)

c01 = (buf[8] << 8) | buf[9]
c01 = twos_complement(c01, 16)
print('c01 =', c01)

c11 = (buf[10] << 8) | buf[11]
c11 = twos_complement(c11, 16)
print('c11 =', c11)

c20 = (buf[12] << 8) | buf[13]
c20 = twos_complement(c20, 16)
print('c20 =', c20)

c21 = (buf[14] << 8) | buf[15]
c21 = twos_complement(c21, 16)
print('c21 =', c21)

c30 = (buf[16] << 8) | buf[17]
c30 = twos_complement(c30, 16)
print('c30 =', c30)

#Write reg 0x06
#i2c.writeto_mem(add, 0x09, b'4')  # Read on A0

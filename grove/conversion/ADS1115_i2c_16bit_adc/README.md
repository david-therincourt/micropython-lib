# Grove - 4 Channel 16-bit ADC (ADS1115)

![](ADS1115.png)

[https://wiki.seeedstudio.com/Grove-16-bit-ADC-ADS1115/](https://wiki.seeedstudio.com/Grove-16-bit-ADC-ADS1115/)

## Without library

```python
from machine import I2C, Pin

#i2c = I2C(freq=400000,sda=Pin(21),scl=Pin(22))   # M5Stack
i2c = I2C(freq=400000, sda=Pin(23), scl=Pin(22))  # Feather ESP32
add = 0x48

i2c.writeto_mem(add, 1, b'\xC2\x85')  # Read on A0

buf = i2c.readfrom_mem(add, 0, 2)
print(buf)
print(bin(buf[0]<<8),bin(buf[1]))
N = buf[0]<<8 | buf[1]
print(N)
U = N*4.096/32767
print(U)
```


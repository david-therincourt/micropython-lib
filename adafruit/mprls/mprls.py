# MicroPython library to support Honeywell MPRLS digital pressure sensors
# David THERINCOURT 2020
# MIT License (MIT)


from time import sleep_ms


class MPRLS:
    def __init__(self, i2c, p_min=0, p_max=25, address=0x18):
        self.i2c = i2c
        self.address = address
        self.p_min = p_min
        self.p_max = p_max        # 25 PSI default
        self.n_min = 0x19999A     # 10% of 2^24
        self.n_max = 0xE66666     # 90% of 2^24
        self.buffer = bytearray(4)

    def read(self):
        """Read pressure in PSI"""
        self.i2c.writeto(self.address, b'\xAA\x00\x00')    # Configuration
        sleep_ms(200)
        self.i2c.readfrom_into(self.address, self.buffer)  # Read data
        n = (self.buffer[1] << 16) | (self.buffer[2] << 8) | self.buffer[3]
        return (n-self.n_min)*(self.p_max-self.p_min)/(self.n_max-self.n_min) + self.p_min
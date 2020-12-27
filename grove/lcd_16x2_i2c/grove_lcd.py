"""
MicroPython library for Pyboard. Only version without RGB backlight.

ported from grove_RCB_LCD.py for circuitpython

ported from rgb_lcd.h & rgb_lcd.cpp made available by SEED Technology Inc.
This provides
The MIT License (MIT)

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
"""

import time


#command values
lcd_cleardisplay = 0x01    # 00000001
lcd_returnhome = 0x02      # 00000010
lcd_entrymodeset = 0x04    # 00000100
lcd_displaycontrol = 0x08  # 00001000
lcd_cursorshift = 0x10     # 00010000
lcd_functionset = 0x20     # 00100000
lcd_set_cg_ram_addr = 0x40 # 01000000
lcd_set_dd_ram_addr = 0x80 # 10000000

#flags for display entry mode
lcd_entry_right = 0x00             # 00000000
lcd_entry_left = 0x02              # 00000010
lcd_entry_shift_increment = 0x01   # 00000001
lcd_entry_shift_decrement = 0x00   # 00000000

#flags for display on/off control
lcd_display_on = 0x04   # 00000100
lcd_display_off = 0x00  # 00000000
lcd_cursor_on = 0x02    # 00000010
lcd_cursor_off = 0x00   # 00000000
lcd_blink_on = 0x01     # 00000001
lcd_blink_off = 0x00    # 00000000

#flags for display/cursor shift
lcd_display_move = 0x08 # 00001000
lcd_cursor_move = 0x00  # 00000000
lcd_move_right = 0x04   # 00000100
lcd_move_left = 0x00    # 00000000

#flags for function set
lcd_8bitmode = 0x10     # 00010000
lcd_4bitmode = 0x00     # 00000000
lcd_2line = 0x08        # 00001000
lcd_1line = 0x00        # 00000000
lcd_5x10dots = 0x04     # 00000100
lcd_5x8dots = 0x00      # 00000000


class Lcd():
    """This is a port of the rgb_lcd.h and rgb_lcd.cpp from the grove seeduino arduino library"""
    def __init__(self, i2c, cols, lines, dotsize = lcd_5x8dots, address = 0x3e ):
        #considered making this a sub-class of I2CDevice, but rgb_lcd needs to actually have 2 devices, not one.
        # define two I2CDevices, one for lcd (self.lcd), one for rgb (self.rgb)
        self.i2c = i2c
        self.address = address
        #create private variables for a specific instance.
        self._displayfunction = 0
        self._displaycontrol = 0
        self._displaymode = 0
        self._initialized = 0
        self._numlines = lines
        self._currline = 0
        if lines > 1:
            self._displayfunction |= lcd_2line
        if (not dotsize == 0) and lines == 1:
            self._displayfunction |= lcd_5x10dots
        #SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION! hitachi HD44780 datasheet
        #according to datasheet, we need at least 40ms after power rises above 2.7V
        #before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
        time.sleep(0.05)
        #according to hitachi hd44780 datasheet
        #send function set command sequence
        self.command(lcd_functionset | self._displayfunction)
        time.sleep(0.0045) #wait more than 4.1 ms
        #second try
        self.command(lcd_functionset | self._displayfunction)
        time.sleep(0.00015)
        #third go
        self.command(lcd_functionset | self._displayfunction)
        #set number of lines, font size, etc
        self.command(lcd_functionset | self._displayfunction)
        #this doesn't make any sense to me why they are tossing the same command 4 times in a row... but it's ported from the rgb_lcd.cpp file provided by seeduino
        #turn the display on with no cursor or blinking default
        self._displaycontrol = lcd_display_on | lcd_cursor_off | lcd_blink_off
        self.display()
        self.clear()
        #initialize to default text direction (for romance languages)
        self._displaymode = lcd_entry_left | lcd_entry_shift_decrement
        #set entry mode
        self.command(lcd_entrymodeset | self._displaymode)


    def clear(self):
        """clear display, set cursor pos to zero"""
        self.command(lcd_cleardisplay)
        time.sleep(0.002) #takes a while (2 microseconds wait)

    def home(self):
        """set cursor position to zero"""
        self.command(lcd_returnhome)
        time.sleep(0.002) #wait 2 milliseconds to execute

    def setCursor(self, col, row):
        """puts cursor at specified location"""
        position = col | 0x80 if row == 0 else col | 0xc0
        dta = bytearray(2)
        dta[0] = 0x80
        dta[1] = position
        self.i2c.writeto(self.address, dta)

    def noDisplay(self):
        """turn the display off (quickly)"""
        self._displaycontrol &= (0xff - lcd_display_on)
        self.command(lcd_displaycontrol | self._displaycontrol)

    def display(self):
        """turn the display on (quickly)"""
        self._displaycontrol |= lcd_display_on
        self.command(lcd_displaycontrol | self._displaycontrol)

    def noCursor(self):
        """turns the underline cursor off"""
        self._displaycontrol &= (0xff - lcd_cursor_on)
        self.command(lcd_displaycontrol | self._displaycontrol)

    def cursor(self):
        """turns the underline cursor on"""
        self._displaycontrol &= (0xff - lcd_cursor_on)
        self.command(lcd_displaycontrol | self._displaycontrol)

    def noBlink(self):
        """turns off blinking cursor"""
        self._displaycontrol |= lcd_cursor_on
        self.command(lcd_displaycontrol | self._displaycontrol)

    def blink(self):
        """turns on the blinking cursor"""
        self._displaycontrol |= lcd_blink_on
        self.command(lcd_displaycontrol | self._displaycontrol)

    def scrollDisplayLeft(self):
        """scroll left without changing the RAM"""
        self.command(lcd_cursorshift | lcd_display_move | lcd_move_left)

    def scrollDisplayRight(self):
        """scroll right without changing the RAM"""
        self.command(lcd_cursorshift | lcd_display_move | lcd_move_right)

    def rightToLeft(self):
        """for text that flows right to left (Hebrew, arabic, or whatever you want)"""
        self._displaymode |= lcd_entry_left
        self.command(lcd_entrymodeset | self._displaymode)

    def autoscroll(self):
        """this will 'right justify' text from the cursor. so, put cursor at the right hand side, send text, and the text will autoscroll to the left from the cursor position (I think.. #todo verify this behavior)"""
        self._displaymode |= lcd_entry_shift_increment
        self.command(lcd_entrymodeset | self._displaymode)

    def noAutoscroll(self):
        """this will 'left justify' text from the cursor"""
        self._displaymode &= (0xff-lcd_entry_shift_increment)
        self.command(lcd_entrymodeset | self._displaymode)

    def createChar(self,location,charmap):
        """allows us to fill the first 8 CGRAM locations with custom characters"""
        location &= 0x7 #essentially the same as modulo operation
        self.command(lcd_set_cg_ram_addr | (location << 3))
        dta = bytearray(9)
        dta[0]=0x40
        for i in range(8):
            dta[i+1] = charmap[i]
        self.i2c_send_bytes(dta)


    def command(self, value):
        """send command"""
        dta = bytearray(2)
        dta[0] = 0x80 #command register address
        dta[1] = value #command byte
        self.i2c_send_bytes(dta)

    def write(self, value):
        """send data"""
        dta = bytearray(2)
        dta[0] = 0x40 #data register address
        dta[1] = value #data byte
        self.i2c_send_bytes(dta)
        return 1 #assume success #also, I don't know why this is the only return in the other source, but there ya go.

    def i2c_send_bytes(self,dta):
        """send a bytearray 'dta' to the lcd address. use setReg for rgb address data transfers"""
        self.i2c.writeto(self.address, dta)

    def print(self, thing):
        """uses str() function on 'thing' and then writes it byte by byte to the lcd"""
        sthing = str(thing)
        for char in sthing:
            self.write(ord(char))

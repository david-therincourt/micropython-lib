# Afficheur Grove I2C LCD v1.0
# Test sur les cartes :
#  - Pyboard
#  - Feather STM32F405 Express
#  - Nucleo 64 STM32F401RE

from machine import I2C
from grove_lcd import Lcd    # Librairie pour Grove I2C LCD V1.2

i2c = I2C(scl="SCL", sda="SDA") # Port I2C
lcd = Lcd(i2c,16,2)    # Afficheur LCD 16x2

lcd.clear()            # Efface l'écran
lcd.print("Bonjour")   # Ecrit un texte à l'emplacement du curseur
lcd.setCursor(0,1)     # Déplace le curseur
lcd.print("MicroPython")    # Ecrit un texte à l'emplacement du curseur

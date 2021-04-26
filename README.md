# MicroPython Library

Libraries for MicroPython on STM32 and ESP32 boards.

## Adrafruit

### Sensor

| Circuit | Interface | Description                      | Status                    |
| ------- | --------- | -------------------------------- | ------------------------- |
| MPRLS   | I2C       | Pressure 0 à 25 PSI (24 bit)     | **OK**                    |

## Grove

### Conversion

| Circuit | Interface | Description                      | Status                    |
| ------- | --------- | -------------------------------- | ------------------------- |
| ADS1115 | I2C       | 4 Channel 16 bit ADC             | **OK**                    |

### Display

| Circuit | Interface | Description                      | Status                    |
| ------- | --------- | -------------------------------- | ------------------------- |
| TM1637  | CLK/DIO   | 4 digit numeric display          | **OK**                    |
| SH1107G | I2C       | OLED 128x128 display             | **Not working**           |
| JHD1804 | I2C       | LCD 16x2                         | **OK**                    |

### LED

| Circuit | Interface | Description                      | Status                    |
| ------- | --------- | -------------------------------- | ------------------------- |
| HT16K33 | I2C       | LED Matrix 8x8                   | **OK**                    |
| MY9221  | I2C       | LED Bar                          | **Not testing**           |
| WS2813  |           | Stick LED RGB                    | **OK**                    |

### Pressure sensor

| Circuit | Interface | Description                                            | Status                    |
| ------- | --------- | -------------------------------------------------- | ------------------------- |
| BME280  | I2C       | Barometer Sensor                                   | **OK**                    |
| BMP280  | I2C       | Barometer Sensor                                   | **OK**                    |
| DPS310  | I2C       | High Precision Barometric Sensor                   | **Not working**           |

### Temperature sensor

| Circuit | Interface | Description                                        | Status                    |
| ------- | --------- | -------------------------------------------------- | ------------------------- |
| ATH20   | I2C       | Industrial Temperature & Humidity Sensor           | **Not testing**           |
| MCP9808 | I2C       | High Accuracy Temperature Sensor                   | **Not testing**           |
| STH35   | I2C       | High Accuracy Temperature & Humidity Sensor        | **Not testing**           |
| TH02    | I2C       | Temperature & Humidity Sensor v1.0                 | **Not testing**           |

## Others

- simple linear regression

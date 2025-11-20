from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime


i2c=I2C(0, sda= Pin(4), scl= Pin(5), freq=400000)

oled=SSD1306_I2C(128,32,i2c)

oled.text('Side Switch', 0, 0)
oled.text('Robot Contact', 0, 10)
oled.text('Test', 0, 20)
oled.show()
utime.sleep(4)
oled.fill (0)
oled.show()

left_button = Pin(20, Pin.IN, Pin.PULL_UP)
right_button = Pin(21, Pin.IN, Pin.PULL_UP)

while True:
    if left_button.value() == 1 and right_button.value() == 1:
        oled.fill (0)
        oled.show()
        oled.text('Lside: Nominal', 0, 0)
        oled.text('Rside: Nominal', 0, 10)
        oled.text('Searching 4 Foe', 0, 20)
        oled.show()
        utime.sleep(1)
    
    elif left_button.value() == 0 and right_button.value() == 1:
        oled.fill (0)
        oled.show()
        oled.text('Lside: Hit', 0, 0)
        oled.text('Rside: Nominal', 0, 10)
        oled.text('Moving Diag FL', 0, 20)
        oled.show()
        utime.sleep(1)
    
    elif left_button.value() == 1 and right_button.value() == 0:
        oled.fill (0)
        oled.show()
        oled.text('Lside: Nominal', 0, 0)
        oled.text('Rside: Hit', 0, 10)
        oled.text('Moving Diag FR', 0, 20)
        oled.show()
        utime.sleep(1)
        
    elif left_button.value() == 0 and right_button.value() == 0:
        oled.fill (0)
        oled.show()
        oled.text('Lside: Hit', 0, 0)
        oled.text('Rside: Hit', 0, 10)
        oled.text('Mommy!', 0, 20)
        oled.show()
        utime.sleep(1)
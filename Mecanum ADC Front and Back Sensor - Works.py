# Raspberry Pi Pico Mecanum Analog Input Test 
# Testing Front and Back Sensors


import machine
import utime

front_sensor = machine.ADC(27) # ADC1 - Physical Pin 32
back_sensor = machine.ADC(28) # ADC2 - Physical Pin 34

while True:
    print("Front Sensor Value: ",front_sensor.read_u16(), end= "  ")
    print("| Back Sensor  Value: ",back_sensor.read_u16(), end= "  ")
    print()
    utime.sleep(1)
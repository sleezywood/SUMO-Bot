# TEJ4M1 - Final Summative (CPT)
# Sumo Robot
# Coded By Faris and Sudhanya
# Wednesday, June 18th, 2025

# Imports for functionality and proper identification of variables
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from machine import Pin, PWM
import utime

# Set pin for each accessory on robot
trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
buzzer = PWM(Pin(19))

i2c=I2C(0, sda= Pin(4), scl= Pin(5), freq=400000)

oled=SSD1306_I2C(128,32,i2c)

# Set song tones and song for buzzer
tones = {
    "GS2": 104,
    "CS7": 2217,
    }

song = ["GS2", "CS7"]

oled.text('Final Summative', 0, 0)
oled.text('Sumo Robot', 0, 10)
oled.show()
utime.sleep(3)
oled.fill (0)

front_sensor = machine.ADC(28) # ADC1 - Physical Pin 32
back_sensor = machine.ADC(27) # ADC2 - Physical Pin 34

#Left Motors (Front and Back)
LF_AO1 = Pin(15,Pin.OUT) # Left Front Must be high to go foward and low to go backward or stop.
LF_AO2 = Pin(14,Pin.OUT) # Left Front Must be low to go foward or stop and high to go backward.
LF_PWMA = PWM(Pin(13))
LB_BO2 = Pin(17,Pin.OUT) # Left Back Pin Must be high to go foward and low to go backward or stop.
LB_BO1 = Pin(16,Pin.OUT) # Left Back Pin Must be low to go foward or stop and high to go backward.
LB_PWMB = PWM(Pin(18))

#Right Motors (Front and Back)
RF_BO1 = Pin(9,Pin.OUT) # Right Front Pin Must be high to go foward and low to go backward or stop.
RF_BO2 = Pin(8,Pin.OUT) # Right Front Pin Must be low to go foward or stop and high to go backward.
RF_PWMB = PWM(Pin(7))
RB_AO2 = Pin(11,Pin.OUT) # Right Back Pin Must be high to go foward and low to go backward or stop.
RB_AO1 = Pin(10,Pin.OUT) # Right Back Pin Must be low to go foward or stop and high to go backward.
RB_PWMA = PWM(Pin(12))

# PWM Frequency
# Setting up motors
LF_PWMA.freq(1000)
LB_PWMB.freq(1000)
RF_PWMB.freq(1000)
RB_PWMA.freq(1000)

LF_PWMA.duty_u16(50536)
LB_PWMB.duty_u16(50536)
RF_PWMB.duty_u16(50536)
RB_PWMA.duty_u16(50536)

# Functions to be called
# Movement functions for the robot
def Forward():
    print("Forward")
    
    LF_AO1.value(1) # Left Front Motor Forward
    LF_AO2.value(0)
    LB_BO2.value(1) # Left Back Motor Forward
    LB_BO1.value(0)
    
    RF_BO1.value(1) # Right Front Motor Forward
    RF_BO2.value(0)
    RB_AO2.value(1) # Right Back Motor Forward
    RB_AO1.value(0)
    
def Backward():
    print("Backward")
    
    LF_AO1.value(0) # Left Front Motor Backwards
    LF_AO2.value(1)
    LB_BO2.value(0) # Left Back Motor Backwards
    LB_BO1.value(1)
    
    RF_BO1.value(0) # Right Front Motor Backwards
    RF_BO2.value(1)
    RB_AO2.value(0) # Right Back Motor Backwards
    RB_AO1.value(1)
    

def StopMotors():
    print("Stop")
    LF_AO1.value(0) # Left Front Motor Stop￼

    LF_AO2.value(0) 
    LB_BO2.value(0) # Left Back Motor Stop
    LB_BO1.value(0)
    
    RF_BO2.value(0) # Right Front Motor Stop
    RF_BO1.value(0)
    RB_AO2.value(0) # Right Back Motor Stop
    RB_AO1.value(0)
    
def LeftPivot():
    print("Left Pivot")
    LF_AO1.value(0) # Left Front Motor Backwards
    LF_AO2.value(1)
    LB_BO2.value(0) # Left Back Motor Backwards
    LB_BO1.value(1)
    
    RF_BO1.value(1) # Right Front Motor Forward
    RF_BO2.value(0)
    RB_AO2.value(1) # Right Back Motor Forward
    RB_AO1.value(0)
    
def RightPivot():
    print("Right Pivot")

    LF_AO1.value(1) # Left Front Motor Forward
    LF_AO2.value(0)
    LB_BO2.value(1) # Left Back Motor Forward
    LB_BO1.value(0)
    
    RF_BO1.value(0) # Right Front Motor Backwards
    RF_BO2.value(1)
    RB_AO2.value(0) # Right Back Motor Backwards
    RB_AO1.value(1)

# Set up IR (infrared) sensors
# Calulate value of front and back sensor
def ir():
    return [str(front_sensor.read_u16()),str(back_sensor.read_u16())]

# Set up and find distance from object to robot using ultrasonic sensor
def ultrasonic_sensor ():
    timePassed = 0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    print("Working")
    while echo.value() == 0:
        low = utime.ticks_us()
        
    while echo.value() == 1:
        high = utime.ticks_us()
        
    timePassed = high - low
    print (timePassed)
    distance_cm = (timePassed*0.0343) / 2  #Calculating the distance in cm.
    # This will print in the Shell as a rounded number. 
    oled.fill(0)
    # In order to show in the OLED, the value must become a string.
    oled.text(str(round(distance_cm,1))+" cm",0,20) 
    oled.show()
    return round(distance_cm,1)

# Functions to play song on buzzer
# Play note
def playtone(frequency):
    buzzer.duty_u16(3500)
    buzzer.freq(frequency)

# Stop playing note
def bequiet():
    buzzer.duty_u16(0)

# Play song on buzzer
def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        utime.sleep(0.3)
    bequiet()
playsong(song)

# Reset robot after code is compiled each time
StopMotors()
song_played = False

# Repeat movements for robot
while True:

    # Gather values of each sensor from robot
    ultrasonic_data = ultrasonic_sensor()
    ir_sensor_data = ir()
    front_sensor_value = int(ir_sensor_data[0])
    back_sensor_value = int(ir_sensor_data[1])
    
    # Print IR sensor values on shell
    print("Front Sensor Value: ", front_sensor_value, end="  ")
    print("| Back Sensor  Value: ", back_sensor_value, end="  ")
    print()
    
    # Movement sequence
    # If front sensor hits boundary, play song and pivot to the right until back sensor hits boundary
    if front_sensor_value > 30000 and back_sensor_value < 30000:
        print("BOUNDARY HIT")
        if not song_played:
            playsong(song)
            song_played = True  # Prevent replaying
        oled.fill(0)
        oled.text("BOUNDARY HIT", 0, 0) # Print that boundary is hit on OLED
        oled.show()
        RightPivot()
        utime.sleep(0.5)
    
    # Move robot forward once back sensor hits boundary to prevent moving out of bounds
    elif front_sensor_value < 30000 and back_sensor_value > 30000:
        Forward()
        print("Back sensor hit, move forward")
        oled.fill(0)
        oled.text("BACK BOUNDARY HIT", 0, 0) # Print that boundary is hit on OLED
        oled.show()
    
    # Scanning sequence if robot does not detect anything
    else:
        if ultrasonic_data > 25:
            print("SCANNING")
            RightPivot()
            oled.fill(0)
            oled.text("SCANNING", 0, 0) # Print that robot is scanning on OLED
            oled.show()
        
        # Attack sequence (move robot forward once ultrasonic sensor detects object)
        else:
            print("ATTACKING")
            Forward()
            oled.fill(0)
            oled.text("ATTACKING", 0, 0) # Print that robot is entering attack sequence on OLED
            oled.show() 
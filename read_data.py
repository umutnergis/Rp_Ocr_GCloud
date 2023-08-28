import time 
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ldr_pin = 3

def RCtime (RCpin):
 reading = 0
 GPIO.setup(RCpin, GPIO.OUT)
 GPIO.output(RCpin, GPIO.LOW)
 time.sleep(.1)
 
 GPIO.setup(RCpin, GPIO.IN)
 while (GPIO.input(RCpin) == GPIO.LOW):
 reading += 1
 return reading
 
while True: 
 LDRReading = RCtime(3)
 print LDRReading
 time.sleep(1)
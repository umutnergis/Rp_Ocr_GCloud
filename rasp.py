import RPi.GPIO as GPIO
import time
import cv2
import datetime
import os

LDR_PIN = 18 # GPIO 18
GPIO.setmode(GPIO.BCM) #GPIO numarical system
GPIO.setup(LDR_PIN, GPIO.IN) #GPIO 18 as input



def take_photo() -> str:

    camera = cv2.VideoCapture(0) 
    if not camera.isOpened():
        print("Error: Could not open camera.")
        exit()
         

    ret, frame = camera.read()

    if ret:
        current_time = time.localtime()
        time_string = time.strftime("%Y-%m-%d_%H-%M-%S", current_time)
        photo_path = f"desktop\photo\{time_string}.jpg"
        cv2.imwrite(photo_path, frame)
        print("Photo taken'.")
        return photo_path
    else:
        print("Photo could not taken.")
    camera.release()

def send_photo(photo_path : str ) ->bool:
    send= True
    if send== False:
        send_photo()

def send_time(elapsed_time : str) -> bool:
    pass 

def idle_for_signal():
    ldr_value = GPIO.input(LDR_PIN)
    while ldr_value == 0:
        ldr_value = GPIO.input(LDR_PIN)
        time.sleep(0.1)

def wait_for_close_signal():
    ldr_value = GPIO.input(LDR_PIN)
    while ldr_value == 1:
        ldr_value = GPIO.input(LDR_PIN)
        time.sleep(0.1)

while True:
    idle_for_signal()
    start_time = datetime.datetime.now()
    photo_path = take_photo()
    if photo_path is None:
        print("Photo not taken.")
        continue
    sended = send_photo(photo_path)   
    while not sended :
        print("Photo not sended.")
        sended = send_photo(take_photo())
    print("Photo sent.")
    wait_for_close_signal()
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    elapsed_time = elapsed_time.total_seconds()
    send_time(elapsed_time)
    os.remove(photo_path)


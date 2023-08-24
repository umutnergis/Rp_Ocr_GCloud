import RPi.GPIO as GPIO
import time
import cv2
import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "raspberry-396713-0cc710728df1.json"
client = vision_v1.ImageAnnotatorClient()
 
LDR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)


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
        print("Fotoğraf çekildi'.")
        return photo_path
    else:
        print("Fotoğraf çekilemedi.")
    camera.release()


def ocr_text(photo_path:str) -> str:
    with open(photo_path, "rb") as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description

def send_data(photo_text:str) -> bool:
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
    
    photo_path = take_photo()
    if photo_path is None:
        print("Fotoğraf çekilemedi.")
        
    else:
        photo_text = ocr_text(photo_path)
        os.remove(photo_path)
    if photo_text is None:
        print("Fotoğraf okunamadı.")
    else:       
        status = send_data(photo_text)
    if status is None:
        print("Veri gönderilemedi.")
    else:
        print("Veri gönderildi.")    
    wait_for_close_signal()
    time.sleep(0.1)
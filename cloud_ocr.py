import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

path = "raspberry-396713-0cc710728df1.json"

class app():
    def __init__(self, json_path: str = None, image_path: str = None):
        self.json_path = f"{json_path}"
        self.image_path = f"{image_path}.jpg"
        self.client = vision_v1.ImageAnnotatorClient()

    def send_photo(self) -> str:
        with open(self.image_path, "rb") as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        response = self.client.text_detection(image=image)
        texts = response.text_annotations
        return texts[0].description
    def print_ocr(self):
        print(self.send_photo())

app = app(path, "photo") # create app object
app.print_ocr() # print ocr result
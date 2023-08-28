import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "raspberry-396713-0cc710728df1.json"
image_path = "denem5.jpg"

client = vision_v1.ImageAnnotatorClient()



with open(image_path, "rb") as image_file:
    content = image_file.read()
image = types.Image(content=content)


response = client.text_detection(image=image)
texts = response.text_annotations


print(texts[0].description)



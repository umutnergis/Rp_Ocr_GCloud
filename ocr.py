import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "raspberry-396713-0cc710728df1.json"

image_path = "photo"
image1 = ""
for file in os.listdir(image_path):
    print(os.listdir(image_path))
    for i in range(len(os.listdir(image_path))):
        image1 = os.listdir(image_path)[i]
        client = vision_v1.ImageAnnotatorClient()

        with open(image1, "rb") as image_file:
            content = image_file.read()
        image = types.Image(content=content)


        response = client.text_detection(image=image)
        texts = response.text_annotations


        print(texts[0].description)
        break
    

   
"""
client = vision_v1.ImageAnnotatorClient()

with open(image1, "rb") as image_file:
    content = image_file.read()

image = types.Image(content=content)


response = client.text_detection(image=image)
texts = response.text_annotations


print(texts[0].description)

----------------------------------------------
 client = vision_v1.ImageAnnotatorClient()

    with open(image1, "rb") as image_file:
        content = image_file.read()
    image = types.Image(content=content)


    response = client.text_detection(image=image)
    texts = response.text_annotations


    print(texts[0].description)

    break


"""
#line = texts[0].description.splitlines()

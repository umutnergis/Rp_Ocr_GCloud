import os
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'smiling-audio-396618-2b29f033f036.json'

client = vision.ImageAnnotatorClient()
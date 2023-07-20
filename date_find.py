from PIL import Image
from PIL.ExifTags import TAGS
import os
def get_time(image):
    image = Image.open(image)
    exifdata = image.getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        if tag == "DateTime":
            print(data)
            return data

for file in os.listdir('od ruby'):
    get_time('od ruby\\' + file)
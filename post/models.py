from django.db import models
import random
from django.conf import settings
import os
from PIL import Image, ExifTags

# Create your models here.
def generateName(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(20))
    return 'images/{randomstring}{ext}'.format(randomstring= randomstr, ext= file_extension)    

def cropper(original_path, x, y, height, width):
    original_path = str(original_path)
    img = Image.open(os.path.join(settings.BASE_DIR, 'media/'+original_path))
    try:
        exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
        print(exif)
        if exif['Orientation']==6:
            img=img.rotate(270, expand=True)
        if exif['Orientation']==8:
            img=img.rotate(90, expand=True)
        if   exif['Orientation']==3: 
            img=img.rotate(180, expand=True)
    except:
        pass
    cropped_image = img.crop((x, y, width+x, height+y))
    resized_image = cropped_image.resize((800, 800), Image.ANTIALIAS)
    resized_image.save(os.path.join(settings.BASE_DIR, 'media/'+ generateName(0, original_path)))
    os.remove(os.path.join(settings.BASE_DIR, 'media/'+original_path))


class imgUpload(models.Model): 
    img = models.ImageField()
    description = models.CharField(max_length=255, blank=True)

   

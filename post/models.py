from django.db import models
import random
from django.conf import settings
import os
from PIL import Image

# Create your models here.
def generateName(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(100))
    return 'images/{randomstring}{ext}'.format(randomstring= randomstr, ext= file_extension)    

def cropper(original_path, x, y, height, width):
    original_path = str(original_path)
    img = Image.open(os.path.join(settings.BASE_DIR, 'media/'+original_path))
    cropped_image = img.crop((x, y, width+x, height+y))
    resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
    resized_image.save(os.path.join(settings.BASE_DIR, 'media/'+ generateName(0, original_path)))
    os.remove(os.path.join(settings.BASE_DIR, 'media/'+original_path))


class imgUpload(models.Model): 
    img = models.ImageField()
    description = models.CharField(max_length=255, blank=True)

   
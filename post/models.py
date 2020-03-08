from django.db import models
import random
import os

# Create your models here.
def generateName(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(10))
    return 'images/{randomstring}{ext}'.format(randomstring= randomstr, ext= file_extension)    

class imgUpload(models.Model): 
    img = models.ImageField(upload_to=generateName)
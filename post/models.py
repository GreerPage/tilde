from django.db import models
import os

# Create your models here.
class imgUpload(models.Model): 
    img = models.ImageField(upload_to='images/')
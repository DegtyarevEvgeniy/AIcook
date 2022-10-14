from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class BaseProduct(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=1000)
    
class Menu(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=1000)
    id_products = models.CharField(max_length=10000)

from django.db import models

# Create your models here.

class BaseProduct(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    basic_taste =  models.CharField(max_length=100)
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    glycemic_index = models.IntegerField()
    calories = models.IntegerField()

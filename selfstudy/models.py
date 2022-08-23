import datetime
from wsgiref.validate import validator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
def current_year():
    return datetime.date.today()
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Ev_halkı(models.Model):
    first_name = models.CharField("Ad",max_length=32)
    last_name = models.CharField("Soyad",max_length=32)
    age = models.IntegerField("Yaş")
    birth_year = models.IntegerField("Doğum yılı",)
    
    def __str__(self) :
        return f"{self.first_name}-{self.last_name}"
    
    class Meta():
        ordering = ["age"]

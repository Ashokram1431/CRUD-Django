from django.db import models
from numpy import integer

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=50,default="")
    Age=models.IntegerField(default="")
    Address=models.CharField(max_length=50,default="")
    Contact=models.IntegerField(default="")
    Mail=models.CharField(max_length=50,default="")


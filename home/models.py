import email
from msilib.schema import Class
from django.db import models

# Create your models here.
class Contect(models.Model):
    email = models.CharField(max_length=100)
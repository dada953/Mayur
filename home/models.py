from django.db import models

# Create your models here.
class Student(models.Model):
    firstName=models.CharField(max_length=14)
    lastName=models.CharField(max_length=10)
    mobileno=models.IntegerField(verbose_name='Mobile No')
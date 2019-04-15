from django.db import models

# Create your models here.
class Prac(models.Model):
    title=models.CharField(max_length=200)
    audience=models.IntegerField(default=0)
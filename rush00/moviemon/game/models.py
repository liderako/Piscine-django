from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=128)
	director = models.CharField(max_length=128)
	year = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	synopsys = models.CharField(max_length=128)
	actors = models.CharField(max_length=4096)

from django.db import models

# Create your models here.
class Link (models.Model):
	name = models.CharField(max_length = 30)
	url = models.URLField(max_length=150)
	program = models.CharField(max_length=10, default=None)
	number = models.CharField(max_length=7, default=None)
	
	
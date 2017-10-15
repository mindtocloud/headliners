from django.db import models

# Create your models here.

class Article(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	description = models.TextField()
	url = models.URLField(max_length=250)
	url_to_image = URLField(max_length=250)
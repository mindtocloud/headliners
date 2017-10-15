from django.db import models

# Create your models here.

class Article(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	description = models.TextField()
	url = models.URLField(max_length=250)
	url_to_image = models.URLField(max_length=250)
	published_at = models.DateTimeField()

# def article_params(data):
# 	return {'author': data['author'], 'title': data['title'], 'description': data['description'], 'url': data['url'], 'url_to_image': data['urlToImage'], 'published_at': data['publishedAt'] }


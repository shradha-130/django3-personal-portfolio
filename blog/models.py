from django.db import models

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=20)
	description=models.TextField(max_length=200)
	url=models.URLField(blank=True)
	# image=models.ImageField(upload_to='blog/images/')

	def __str__(self):
		return self.title
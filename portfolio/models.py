from django.db import models

class Profile(models.Model):
	title= models.CharField(max_length=20)
	description= models.CharField(max_length=40)
	image=models.ImageField(upload_to='portfolio/images/')
	url=models.URLField(blank=True)

	def __str__(self):
		return self.title
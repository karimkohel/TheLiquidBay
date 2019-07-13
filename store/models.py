from django.db import models

# Create your models here.

class Liquid(models.Model):
	name = models.CharField(max_length=100)
	contents = models.TextField()
	image = models.ImageField(default='default_liquid.jpg',upload_to='liquid_pics')

	def __str__(self):
		return self.name
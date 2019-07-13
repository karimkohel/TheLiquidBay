from django.db import models
from django.contrib.auth.models import User
from .choices import *
from PIL import Image

# Create your models here.

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default_profile.jpg',upload_to='profile_pics')
	city = models.CharField(max_length=2, choices=CITY, default=CAIRO)
	adress = models.TextField(default="")


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
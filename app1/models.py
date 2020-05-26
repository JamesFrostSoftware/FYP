from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
	title = models.CharField(max_length=30)
	director = models.CharField(max_length=30, default='0000000')
	desc = models.TextField()
	releaseDate = models.DateTimeField()
	cont = models.ForeignKey(User, on_delete=models.CASCADE)
		
	def __str__(self):
		return self.title
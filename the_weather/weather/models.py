from django.db import models

# Create your models here.
# interface for views index functions and template weather html file in 
# models to display multiple cities and register models in admin file
# **models file also used for database**
class City(models.Model):
	"""docstring for city"""
	name = models.CharField(max_length=25)
	def __str__(self):
		return self.name
		
		class Meta:
			"""docstring for Meta"""
			verbose_name_plural = 'cities'
		
				


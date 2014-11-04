from django.db import models

class Book(models.Model):
	name						= models.CharField(max_length=50)
	number					= models.PositiveSmallIntegerField()
	isbn						= models.CharField(max_length=13)
	datepublished			= models.DateField(auto_now=False, auto_now_add=False)
	
	def __unicode__(self):
		return self.name



from django.db import models
from tinymce import models as tinymce_models

class AllBooks(models.Model):
	name						= models.CharField(max_length=50)
	number					= models.PositiveSmallIntegerField()
	isbn						= models.CharField(max_length=13)
	datepublished			= models.DateField(auto_now=False, auto_now_add=False)
	content 					= tinymce_models.HTMLField()
	
class TheBigJob(models.Model):
	name						= models.CharField(max_length=50)
	number					= models.PositiveSmallIntegerField()
	isbn						= models.CharField(max_length=13)
	datepublished			= models.DateField(auto_now=False, auto_now_add=False)
	
	def __unicode__(self):
		return self.name



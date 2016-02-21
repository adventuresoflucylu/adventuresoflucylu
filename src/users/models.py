from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	website = models.URLField(blank=True)
	doggiesname	= models.CharField(max_length=20, blank=True)
	picture		= models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

class BookUser(models.Model):
#	user = models.ForeignKey(User)
#	user = models.ManyToManyField("self")
#	user = models.ManyToManyField(User)
	user		= models.OneToOneField(settings.AUTH_USER_MODEL)
	name 		= models.CharField(max_length=100)
	email 	= models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title


# create our user object to attach to ourBookUser object
def create_bookuser_user_callback(sender, instance, **kwargs):
#	users, new = BookUser.objects.get_or_create(user=instance)
	users, new = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_bookuser_user_callback, User)

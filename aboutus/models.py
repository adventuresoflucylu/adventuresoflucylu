from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Books(models.Model):
	pass

# create our user object to attach to ourBookUser object
#def create_aboutus_user_callback(sender, instance, **kwargs):
#	users, new = Books.objects.get_or_create(user=instance)
#	users, new = Books.objects.get_or_create(user=instance)
#post_save.connect(create_aboutus_user_callback, User)



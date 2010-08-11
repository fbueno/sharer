from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User,unique=True)
	activation_key = models.CharField(max_length=56)
	key_expires = models.DateTimeField()
        def __unicode__(self):
                return self.user.username

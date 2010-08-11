from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
	user = models.ForeignKey(User,unique=False, primary_key=False)
	f = models.FileField('File', upload_to='./shared/', blank=False, null=False)
	key =  models.CharField(max_length=6, blank=False, null=False, unique=True)
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
        	return self.f.name

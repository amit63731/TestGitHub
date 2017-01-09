from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.
class Histograph(models.Model):
	letter = models.CharField(max_length=1)
	frequency = models.FloatField()

	def __unicode__(self):
		return smart_unicode(self.letter)


#class SignUp(models.Model):
#	first_name = models.CharField(max_length=120, null=True, blank=True)
#	last_name = models.CharField(max_length=120, null=True, blank=True)
#	email = models.EmailField()
#	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#	def __unicode__(self):
#		return smart_unicode(self.email)

class SignUp(models.Model):
	first_name = models.CharField(max_length=120,null=True, blank=True, unique=True)
	last_name = models.CharField(max_length=120, null=True,blank=True)
	email = models.EmailField(default="dummy@dummy.com")
	
	def __unicode__(self):
		return smart_unicode(self.first_name)


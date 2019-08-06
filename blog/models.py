from django.db import models
import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver


def generate_filename(self, filename):
	date_time = datetime.datetime.now()
	url = "blog/{0}_{1}".format(date_time, filename)
	return url

class post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	image = models.FileField(upload_to=generate_filename, blank=True)
	
	#object title
	def __str__(self):
		return "{}".format(self.title)

#delete media when object deleted
#sender = model class
#image = FileField name
@receiver(post_delete, sender=post)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False) 
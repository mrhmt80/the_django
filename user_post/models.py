from django.db import models
import datetime

def generate_filename(self, filename):
	date_time = datetime.datetime.now()
	url = "user_post/{0}_{1}".format(date_time, filename)
	return url

class UserPost(models.Model):
   nama = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = generate_filename)

   def __str__(self):
   		return "{}".format(self.nama)

class Meta:
	db_table = "user_post"


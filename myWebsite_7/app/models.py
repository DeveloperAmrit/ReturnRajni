from django.db import models
import django.utils.timezone
import django.db.models
# Create your models here.

class video(models.Model):
    title = models.CharField(max_length=100,default='CLIP')
    video = models.FileField(upload_to='videos/',default='DEFAULT_MODEL')

class feedback(models.Model):
    feedbacker = models.CharField(max_length=30, default='DEFAULT')
    feedbacker_userid = models.CharField(max_length=30, default='DEFAULT')
    feedbacker_email = models.EmailField(max_length=100,default='none@gmail.com')
    feedback = models.CharField(max_length=600,default='NO FEEDBACK')
    published_date = models.DateField(default= django.utils.timezone.now)
        
    def __str__(self):
        return self.feedbacker_email
from django.db import models
from django.utils.timezone import now
# from django.contrib.auth.models import User

# Create your models here.

# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     signup_date = models.DateTimeField()
    
class Notes(models.Model):
    title = models.CharField(max_length=1023, default="")
    content = models.CharField(max_length=65535, default="")
    last_updated = models.DateTimeField(default=now)
    date_created = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)
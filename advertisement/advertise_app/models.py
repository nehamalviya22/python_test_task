from django.db import models

# Create your models here.
class username(models.Model):
    username = models.CharField(max_length=100)
    ad_count = models.IntegerField(default=0)
    impression_count = models.IntegerField(default=0)

class sdkversion(models.Model):
    sdkversion = models.CharField(max_length=100)
    ad_count = models.IntegerField(default=0)
    impression_count = models.IntegerField(default=0)
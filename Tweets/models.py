from django.db import models

class Tweet(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=150)
    user = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    score = models.IntegerField()
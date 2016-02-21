from django.db import models


class Tweet(models.Model):
    date = models.DateTimeField(null=True)
    content = models.CharField(max_length=150)
    user = models.CharField(max_length=30)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    score = models.IntegerField(null=True)

    def __str__(self):
        return "%s" % (self.content)
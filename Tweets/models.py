from django.db import models

class Region(models.Model):
    location = models.CharField(max_length=50)
    subunit = models.IntegerField()
    pulled = models.BooleanField(default=False)
    tweetScore = models.FloatField(null=True)
    finalScore = models.FloatField(null=True)
    adjacent = models.ManyToManyField("self", blank=True, null=True)

    def __str__(self):
        return "%s" % (str(self.subunit))

class Tweet(models.Model):
    date = models.DateTimeField(null=True)
    content = models.CharField(max_length=150)
    user = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default="")
    score = models.FloatField(null=True)

    def __str__(self):
        return "%s" % (self.content)
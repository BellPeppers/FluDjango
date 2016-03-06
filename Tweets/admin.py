from django.contrib import admin
from .models import Tweet, Region
from .tweetHelper import tweetPull, adjacentRegions, regionCreator, analysis, gatherTweetScore, calcFinalScore
# Register your models here.

# Admin login: username is admin, password is admin0123.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tweet', {'fields': ['content']}),
        ('User', {'fields': ['user']}),
        ('Date', {'fields': ['date']}),
        ('Score', {'fields': ['score']}),
        ('Region', {'fields': ['region']}),
    ]

class RegionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subunit', {'fields': ['subunit']}),
        ('Coordinates', {'fields': ['location']}),
        ('Pulled', {'fields': ['pulled']}),
        ('Tweet score', {'fields': ['tweetScore']}),
        ('Final score', {'fields': ['finalScore']}),
        ('Adjacent regions', {'fields': ['adjacent']}),
    ]

admin.site.register(Tweet,TweetAdmin)
admin.site.register(Region,RegionAdmin)

# regionCreator()
# adjacentRegions()
# tweetPull()
# analysis()
# gatherTweetScore()
# calcFinalScore()

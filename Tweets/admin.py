from django.contrib import admin
from .models import Tweet, Region
from.tweetHelper import test
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
        ('Score', {'fields': ['score']}),
    ]

admin.site.register(Tweet,TweetAdmin)
admin.site.register(Region,RegionAdmin)
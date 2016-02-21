from django.contrib import admin
from .models import Tweet
from .tweetHelper import tweetPull
# Register your models here.

# Admin login: username is admin, password is admin0123.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tweet', {'fields': ['content']}),
        ('User', {'fields': ['user']}),
        ('Date', {'fields': ['date']}),
        ('Score', {'fields': ['score']}),
    ]

admin.site.register(Tweet,TweetAdmin)

tweetPull()


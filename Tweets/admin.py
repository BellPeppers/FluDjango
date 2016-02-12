from django.contrib import admin
from .models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tweet', {'fields': ['content']}),
        ('User', {'fields': ['user']}),
        ('Date', {'fields': ['date']}),
        ('Score', {'fields': ['score']}),
    ]

admin.site.register(Tweet,TweetAdmin)


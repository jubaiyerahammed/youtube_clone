from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    banner_image = models.URLField(blank=True, null=True)

    is_channel_verified = models.BooleanField(default=False)
    subscribers_count = models.IntegerField(default=0)

    description = models.TextField()

    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True)  
    # Example: {"facebook": "...", "instagram": "...", "twitter": "..."}

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # FIXED

    def __str__(self):
        return self.name

class VideoContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    # Thumbnail + Video URL
    thumbnail = models.URLField()
    video_url = models.URLField()

    # Relations
    channel = models.ForeignKey('channel', on_delete=models.CASCADE, related_name='videos')

    # Stats
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    duration = models.CharField(max_length=20)  # Example: "12:45"

    # Extra info
    is_premium = models.BooleanField(default=False)
    category = models.CharField(max_length=100, default="General")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.URLField()
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    


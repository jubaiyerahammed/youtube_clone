

# Create your models here.
from django.db import models

class Short(models.Model):
    title = models.CharField(max_length=100)
    views = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='shorts/', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True,)

    video_url = models.URLField(blank=True, null=True) 

    
    def __str__(self):
        return self.title

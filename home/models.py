from django.db import models

# Create your models here.
from django.db import models
class TagTitels (models.Model):
    titel = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

from django.db import models

class Journal(models.Model):
    name = models.CharField(max_length = 100)
    content = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    content_image = models.ImageField(upload_to='content_images', blank=True, null=True)

    def __str__(self):
        return self.name

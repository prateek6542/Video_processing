from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    subtitle = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.title

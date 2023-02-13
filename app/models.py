from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill



class BodyProgress(models.Model):
    body_weight = models.DecimalField(max_digits=5, decimal_places=1)
    biceps = models.CharField(max_length=200)
    chest = models.CharField(max_length=200)
    legs = models.CharField(max_length=200)
    waist = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    img = ProcessedImageField(upload_to='user-images',
                              processors=[ResizeToFit(1920, 1920)],
                              format='JPEG',
                              options={'quality': 100},
                              blank=True, null=True)
    profile_pictures = ImageSpecField(source='img',
                                      processors=[ResizeToFill(65, 65)],
                                      format='JPEG',
                                      options={'quality': 80})
    created_at = models.DateTimeField()
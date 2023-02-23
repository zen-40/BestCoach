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
                              processors=[ResizeToFit(980, 980)],
                              format='JPEG',
                              options={'quality': 100})
    profile_pictures = ImageSpecField(source='img',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 80})
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']



class Meal(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    more = models.CharField(max_length=200)
    img = ProcessedImageField(upload_to='user-images',
                              processors=[ResizeToFit(1920, 1920)],
                              format='JPEG',
                              options={'quality': 100})
    profile_pictures = ImageSpecField(source='img',
                                      processors=[ResizeToFill(80, 80)],
                                      format='JPEG',
                                      options={'quality': 100})
    special_img = ImageSpecField(source='img',
                                      processors=[ResizeToFill(585, 265)],
                                      format='JPEG',
                                      options={'quality': 100})



class Training(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    img = ProcessedImageField(upload_to='user-images',
                              processors=[ResizeToFit(1920, 1920)],
                              format='JPEG',
                              options={'quality': 100},
                              blank=True, null=True)
    profile_pictures = ImageSpecField(source='img',
                                      processors=[ResizeToFill(80, 80)],
                                      format='JPEG',
                                      options={'quality': 100})
    sets = models.CharField(max_length=200)
    repeats = models.CharField(max_length=200)



class ChatSample(models.Model):
    content = models.TextField()

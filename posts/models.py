from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'name', blank=False, null=False, max_length=14, db_index=True, default='anonymous'
    )  
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )   
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    ) 
    image = CloudinaryField(
        'image', blank=True, null=True 
    )

    like_count = models.PositiveIntegerField(
        'Like Count', default=0, blank=True
    ) 
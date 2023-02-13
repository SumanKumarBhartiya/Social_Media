from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profile_photo=models.ImageField(upload_to='profile_images',default='profile.webp')
    cover_photo=models.ImageField(upload_to='cover_images',default='coverphoto.png')
    intro=models.TextField(max_length=100,default="")
    education=models.TextField(max_length=100,default="")
    hometown=models.TextField(max_length=50,default="")
    work=models.TextField(max_length=100,default="")

    def __str__(self):
        return self.user.username


class PostlLike(models.Model):
    pass
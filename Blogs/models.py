from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='images')
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
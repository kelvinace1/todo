from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    #title = models.CharField(max_length=20, null = True)
    content = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
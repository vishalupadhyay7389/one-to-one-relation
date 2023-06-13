from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user_id = models.IntegerField(unique=True)
    user_post = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.CharField(max_length=90)
    lname = models.CharField(max_length=90)
    date_of_post = models.DateField()
    date_time = models.DateTimeField()

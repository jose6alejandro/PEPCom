from django.db import models

# Create your models here.
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
   return '%s/%s' % (instance.user.username, filename)

class User_Create_Problem(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

   name = models.CharField(max_length=60)

   question = models.CharField(max_length=200)

   correct_option = models.CharField(max_length=70)
   distractor1 = models.CharField(max_length=70)
   distractor2 = models.CharField(max_length=70)
   distractor3 = models.CharField(max_length=70)

   explanation = models.CharField(max_length=250)

   image = models.ImageField(upload_to=user_directory_path, null = True)

   abstraction = models.BooleanField(blank=True)
   decomposition = models.BooleanField(blank=True)
   algorithms = models.BooleanField(blank=True)
   generalization = models.BooleanField(blank=True)
   evaluation = models.BooleanField(blank=True)

   
   def __str__(self):
      return '%s' % (self.name)
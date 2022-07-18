from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Problems_Completed(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)

   name = models.CharField(max_length=60)
   
   def __str__(self):
      return '%s' % (self.name)
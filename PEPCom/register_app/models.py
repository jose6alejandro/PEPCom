from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class User_Profile(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)

   birthday_date = models.DateField()
   access_code = models.CharField(max_length=10)
   user_role = models.BooleanField()
   
   def __str__(self):
      return '%s, %s, %s' % (self.birthday_date, self.access_code, self.user_role)

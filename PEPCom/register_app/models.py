from django.db import models

# Create your models here.

class User_register(models.Model):
	
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	email_user = models.EmailField()
	user_password = models.CharField(max_length=40)
	birthday_date = models.DateField()
	access_code = models.CharField(max_length=10)
	user_role = models.BooleanField()

	def __str__(self): #visualizar algunos datos
		return '%s, %s, %s, %s, %s, %s, %s' % (self.first_name, self.last_name, self.email_user,
			self.user_password, self.birthday_date, self.access_code, self.user_role)

	#objects = models.Manager()


# a =  User_register.objects.create(first_name='luis', last_name='Salazar', email_user='hasdh@gmail.com', user_password='asdbn', birthday_date='1998-10-10', access_code='123a', user_role=True)

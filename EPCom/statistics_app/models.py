from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class My_Skills(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

   score = models.IntegerField(default=0, blank=True)
   abstraction = models.IntegerField(default=0, blank=True)
   decomposition = models.IntegerField(default=0, blank=True)
   algorithms = models.IntegerField(default=0, blank=True)
   generalization = models.IntegerField(default=0, blank=True)
   evaluation = models.IntegerField(default=0, blank=True)
   attempts = models.IntegerField(default=0, blank=True)
   correct_answers = models.IntegerField(default=0, blank=True)

   def __str__(self):
      return 'score: %i, usuario: %s' % (self.score, self.user)

class My_Performance(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	
	january = models.IntegerField(default=0, blank=True)
	february = models.IntegerField(default=0, blank=True)
	march = models.IntegerField(default=0, blank=True)
	april = models.IntegerField(default=0, blank=True)
	may = models.IntegerField(default=0, blank=True)
	june = models.IntegerField(default=0, blank=True)
	july = models.IntegerField(default=0, blank=True)
	august = models.IntegerField(default=0, blank=True)
	september = models.IntegerField(default=0, blank=True)
	october = models.IntegerField(default=0, blank=True)
	november = models.IntegerField(default=0, blank=True)
	december = models.IntegerField(default=0, blank=True)

	def __str__(self):
		return 'usuario: %s' % (self.user)

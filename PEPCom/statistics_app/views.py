from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
#from crud_problems_app.models import User_Create_Problem
#from register_app.models import User_Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required()
def my_stats(request):
	return render(request, 'personal_stats.html')
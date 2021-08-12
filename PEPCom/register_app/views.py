from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from .forms import Form_Login, Form_Register
from django.contrib.auth.decorators import login_required
from register_app.models import User_register

def login(request):
   
   form = Form_Login(request.POST  or None)
   form1 = Form_Register(request.POST or None)
   
   alert = None
   success = True

   if request.method=='POST':

      if form.is_valid():
         inf_login = form.cleaned_data
         search_user = User_register.objects.filter(email_user = inf_login['email'],
             user_password = inf_login['password'])
         if search_user:
            return redirect('home')

      if form1.is_valid():

         inf_register = form1.cleaned_data
         search_email = User_register.objects.filter(email_user = inf_register['email_user'])
         #search_code = User_register.objects.filter(access_code = inf_register['access_code'])
         if search_email:
            alert = 'El correo eletrónico ya existe, intente de nuevo'
            success = False
         else:
            alert = 'Registro exitoso, ahora puede iniciar sesión'
            success = True  
            save_register = User_register(first_name=inf_register['first_name'], last_name=inf_register['last_name'],
               email_user=inf_register['email_user'], user_password=inf_register['user_password'], 
               birthday_date=inf_register['birthday_date'], access_code=inf_register['access_code'],
               user_role=inf_register['user_role'] )
            save_register.save()
      else:
         alert = 'Datos invalidos, intente de nuevo'
         success = False  
      
      form1 = Form_Register()

   return render(request,'accounts/login.html', {"form": form,"alert": alert, "success": success, "form1": form1})

@login_required
def home(request):
   return render(request, 'home.html')  
      

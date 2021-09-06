from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from .forms import Form_Login, Form_Register
from register_app.models import User_Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import distutils
from distutils import util

def login_view(request):
   
   form = Form_Login(request.POST)
   form1 = Form_Register(request.POST)
   alert = None
   success = False
   flag =  False

   if request.method == "POST":
      
      if form.is_valid():
         
         username = form.cleaned_data.get("username")
         password = form.cleaned_data.get("password")
         user = authenticate(username=username, password=password)

         if user is not None:
            login(request, user)
            return redirect("home")
         else:    
            alert = 'Datos incorrectos, intente de nuevo'    
      else:
         alert = 'Error en la validación' 

      if form1.is_valid():   

         inf_register = form1.cleaned_data

         search_code = User.objects.filter(user_profile__user_role="False", 
                                          user_profile__access_code=inf_register["access_code"])

         if bool(distutils.util.strtobool(inf_register['user_role'])): # is student?

            if not search_code:
               alert = 'El código no existe, intente de nuevo'
               flag = True 
         else:

            if search_code:
               alert = 'El código ya existe, intente de nuevo'
               flag = True                
         
         username = inf_register["email_user"]
         search_user = User.objects.filter(username = username)

         if search_user or flag: # validate email and access_code
            if search_user:
               alert = 'El correo eletrónico ya existe, intente de nuevo'

            success = False
         else:
            alert = 'Registro exitoso, ahora puede iniciar sesión'
            success = True  
            user = User.objects.create_user(username, 
                                          inf_register["email_user"], 
                                          inf_register["user_password"],
                                          first_name = inf_register["first_name"],
                                          last_name=inf_register["last_name"])
            user.save()
            user_add = User_Profile.objects.create(user=user, 
                                                   birthday_date = inf_register['birthday_date'],
                                                   access_code = inf_register['access_code'], 
                                                   user_role = inf_register['user_role'])  
            user_add.save()
            #print(user.user_profile_set.all())
      else:
         alert = 'Datos invalidos, intente de nuevo'
         success = False  

      form1 = Form_Register()   
      
   return render(request, "accounts/login.html", 
               {"form": form, 
               "form1": form1,
               "alert" : alert,
               "success": success})


def redirect_home(request):
   return redirect("home") 

@login_required()
def home(request):
   return render(request, 'home.html')  
   

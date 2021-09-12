from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from .forms import Form_Login, Form_Register
from register_app.models import User_Profile
from statistics_app.models import My_Skills, My_Performance
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import distutils
from distutils import util
from datetime import date
from django.contrib import messages


def check(user):
    return user.user_profile_set.get().user_role

def check_not(user):
    return not user.user_profile_set.get().user_role

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
            messages.error(request, "Datos incorrectos, intente de nuevo")    
      else:
         messages.error(request, "Error en la validación")    

      if form1.is_valid():   

         inf_register = form1.cleaned_data

         search_code = User.objects.filter(user_profile__user_role="False", 
                                          user_profile__access_code=inf_register["access_code"])

         if bool(distutils.util.strtobool(inf_register['user_role'])): # is student?

            if not search_code:
               messages.error(request, "El código de acceso no existe, intente de nuevo")
               flag = True 
         else:

            if search_code:
               messages.error(request, "El código de acceso ya existe, intente de nuevo")
               flag = True                
         
         username = inf_register["email_user"]
         search_user = User.objects.filter(username = username)

         if search_user or flag: # validate email and access_code
            if search_user:
               messages.error(request, "El correo eletrónico ya existe, intente de nuevo")
         else:
            messages.success(request, "Registro exitoso, ahora puede iniciar sesión")
 
            user = User.objects.create_user(username, 
                                          inf_register["email_user"], 
                                          inf_register["user_password"],
                                          first_name = inf_register["first_name"],
                                          last_name = inf_register["last_name"])
            user.save()
            user_add = User_Profile.objects.create(user=user, 
                                                   birthday_date = inf_register['birthday_date'],
                                                   access_code = inf_register['access_code'], 
                                                   user_role = inf_register['user_role'])  
            user_add.save()
            
      else:
         messages.error(request, "Datos invalidos, intente de nuevo")


      form1 = Form_Register()   
      
   return render(request, "accounts/login.html", 
               {"form": form, 
               "form1": form1})


def redirect_home(request):
   return redirect("home") 


@login_required()
def home(request):
   
   if request.user.user_profile_set.get().user_role:  

      search_user = My_Skills.objects.filter(user_id=request.user.id)
      
      if not search_user:
         user = My_Skills.objects.create(user_id = request.user.id)
         
         user.save()

      search_user_aux = My_Performance.objects.filter(user_id=request.user.id)

      if not search_user_aux:
         user = My_Performance.objects.create(user_id = request.user.id)
         user.save()

      actual = date.today().month
      last_login = request.user.last_login.month

      if actual == last_login:

         user_performance = request.user.my_skills_set.get()
         month_performance = request.user.my_performance_set.get()
         total_performance = 0

         if user_performance.attempts != 0:
            total_performance = (user_performance.correct_answers / user_performance.attempts) * 100       


         if actual == 1:
            month_performance.january = total_performance
         elif actual == 2:
            month_performance.february = total_performance
         elif actual == 3:
            month_performance.march = total_performance
         elif actual == 4:
            month_performance.april = total_performance
         elif actual == 5:
            month_performance.may = total_performance
         elif actual == 6:
            month_performance.june = total_performance
         elif actual == 7:
            month_performance.july = total_performance
         elif actual == 8:
            month_performance.august = total_performance
         elif actual == 9:
            month_performance.september = total_performance                                
         elif actual == 10:
            month_performance.october = total_performance 
         elif actual == 11:
            month_performance.november = total_performance 
         else:
            month_performance.december = total_performance

         month_performance.save()    
      else:
         user_performance.correct_answers = 0
         user_performance.attempts = 0
         user_performance.save()

      actual_year = date.today().year
      last_login_year = request.user.last_login.year

      if actual_year != last_login_year:
         
         month_performance.january = 0
         month_performance.february = 0
         month_performance.march = 0
         month_performance.april = 0
         month_performance.may = 0
         month_performance.june = 0
         month_performance.july = 0
         month_performance.august = 0
         month_performance.september = 0
         month_performance.october = 0
         month_performance.november = 0
         month_performance.december = 0

         month_performance.save() 

   else:
      pass
      #print("EL USUARIO ES PROFESOR")
   
   return render(request, 'home.html')  
   
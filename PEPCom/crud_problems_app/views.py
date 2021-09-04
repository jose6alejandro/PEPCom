from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import Form_Create_problem
from django.contrib.auth.models import User
from crud_problems_app.models import User_Create_Problem
from PIL import Image, ImageOps
import distutils
from distutils import util
import os
from django.conf import settings
from django.contrib import messages

@login_required()
def read_problems(request):
   info_problems = User_Create_Problem.objects.filter(user_id=request.user.id)

   return render(request, 'read.html', {"info": info_problems})


@login_required()
def create_problems(request):

   data = {
      "form": Form_Create_problem()
   }
   
   if request.method == "POST":

      info_form = Form_Create_problem(data=request.POST, files=request.FILES)

      if info_form.is_valid():
         instance = info_form.save(commit=False)
         instance.user = request.user
         instance.image.name = instance.name + ".png"
         instance.save()
         messages.success(request, "Registrado correctamente")
         return redirect("read")
      else:
         data["form"] = info_form

   return render(request, 'create.html', data)


@login_required()
def update_problems(request, id):
   
   id_problem = get_object_or_404(User_Create_Problem, id=id)

   data = {
      "form": Form_Create_problem(instance=id_problem)
   }
   temp = id_problem.image.name
   if request.method == "POST":

      info_form = Form_Create_problem(data=request.POST, instance=id_problem,files=request.FILES)

      if info_form.is_valid():
         instance = info_form.save(commit=False)
         instance.user = request.user

         if len(request.FILES)!=0:
            os.remove(settings.MEDIA_ROOT+"/"+temp) #delete old_image

         instance.save()
         messages.success(request, "Problema modificado correctamente")
         return redirect("read")
      else:
         data["form"] = info_form


   return render(request, 'update.html', data) 

@login_required()
def delete_problems(request, id):
   
   id_problem = get_object_or_404(User_Create_Problem, id=id)
   os.remove(settings.MEDIA_ROOT+"/"+id_problem.image.name) #delete image 
   id_problem.delete()
   return redirect("read")
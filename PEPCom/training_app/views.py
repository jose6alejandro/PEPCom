from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from crud_problems_app.models import User_Create_Problem
from register_app.models import User_Profile
from django.contrib.auth.decorators import login_required
import random
from django.contrib import messages

@login_required()
def practice_problem(request):
    user_active = request.user.user_profile_set.get()

    user_teacher =User_Profile.objects.filter(access_code=user_active.access_code, user_role=False)

    if request.method == "POST":
        select_option = request.POST.get("value")
        correct = request.POST.get("correct")

        #if select_option is None:

        name = request.user.first_name

        if select_option == correct:
            messages.success(request, "Muy bien, "+ name)
            #create model
        else:
            messages.error(request, "Ouh, la respuesta es incorrecta")

        return redirect("question")
    else:
        problems = list(User_Create_Problem.objects.filter(user_id=user_teacher[0].user_id))
        
        select_problem = random.choice(problems)

        list_options = [select_problem.correct_option, select_problem.distractor1, 
                    select_problem.distractor2, select_problem.distractor3]
        
        random_options = random.sample(list_options, len(list_options))

        correct_option = select_problem.correct_option

    return render(request, 'question.html',
                {"problem": select_problem, 
                "option": random_options, 
                "correct": select_problem.correct_option
                })
    
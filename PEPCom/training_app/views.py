from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from crud_problems_app.models import User_Create_Problem
from statistics_app.models import My_Skills
from register_app.models import User_Profile
from training_app.models import Problems_Completed
from django.contrib.auth.decorators import login_required, user_passes_test
import random
from django.contrib import messages
import distutils
from distutils import util
from register_app import views

@login_required()
@user_passes_test(views.check, login_url= '/home/')
def practice_problem(request):
    user_active = request.user.user_profile_set.get()

    user_teacher =User_Profile.objects.filter(access_code=user_active.access_code, user_role=False)

    if request.method == "POST":
        name_problem = request.POST.get("name_problem")
        select_option = request.POST.get("value")
        correct = request.POST.get("correct")
        explanation = request.POST.get("explanation")
        
        update = My_Skills.objects.filter(user_id=request.user.id)[0]

        if select_option is None:
            id_ = request.POST.get("id")
            problems = list(User_Create_Problem.objects.filter(id=int(id_)))
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
        else:
            update.attempts += 1

        name = request.user.first_name

        if select_option == correct:

            p_completed = Problems_Completed.objects.create(name=name_problem, user_id=request.user.id)
            p_completed.save()
            
            update.score += 25
            update.correct_answers += 1

            if bool(distutils.util.strtobool(request.POST.get("abstraction"))):
                update.abstraction += 1

            if bool(distutils.util.strtobool(request.POST.get("decomposition"))):
                update.decomposition += 1

            if bool(distutils.util.strtobool(request.POST.get("algorithms"))):
                update.algorithms += 1

            if bool(distutils.util.strtobool(request.POST.get("generalization"))):
                update.generalization += 1

            if bool(distutils.util.strtobool(request.POST.get("evaluation"))):
                update.evaluation += 1

            messages.success(request, explanation)

        else:
            messages.error(request, "Ouh, la respuesta es incorrecta")
        
        update.save()
        
        return redirect("question")
    else:
        try:
            p_completed = Problems_Completed.objects.filter(user_id=request.user.id)
            p_completed = [i.name for i in p_completed] 

            problems = list(User_Create_Problem.objects.filter(user_id=user_teacher[0].user_id).exclude(name__in=p_completed))

            select_problem = random.choice(problems)

            list_options = [select_problem.correct_option, select_problem.distractor1, 
                    select_problem.distractor2, select_problem.distractor3]
        
            random_options = random.sample(list_options, len(list_options))

            correct_option = select_problem.correct_option
        except:
            messages.info(request, "No hay problemas disponibles, vuelva más tarde")
            return redirect("home")    

    return render(request, 'question.html',
                {"problem": select_problem, 
                "option": random_options, 
                "correct": select_problem.correct_option
                })
    
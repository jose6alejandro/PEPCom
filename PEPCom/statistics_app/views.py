from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.models import User
from register_app.models import User_Profile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from statistics_app.models import My_Skills, My_Performance
from datetime import date
from register_app import views

@login_required()
@user_passes_test(views.check, login_url= '/home/')
def my_stats(request):  

    title = 'Mis estadísticas'
    user_skills = request.user.my_skills_set.get()
    user_performance = request.user.my_performance_set.get()
    year = date.today().year
    total_skills_value = (
                        user_skills.abstraction + 
                        user_skills.decomposition + 
                        user_skills.algorithms + 
                        user_skills.generalization + 
                        user_skills.evaluation
                        )


    return render(request, 'personal_stats.html', {
                                                    "skill": user_skills,
                                                    "performance": user_performance,
                                                    "total": total_skills_value,
                                                    "year": year,
                                                    "title": title
                                                    })


@login_required()
@user_passes_test(views.check_not, login_url= '/home/')
def view_select_stats(request, id): 
    
    user_id = get_object_or_404(User, id=id)
    year = date.today().year    
    user_skills = None
    user_performance = None

    try:
       user_skills = user_id.my_skills_set.get()
       user_performance = user_id.my_performance_set.get()
    except:
        messages.info(request, "El usuario todavía no tiene estadísticas")
        return redirect("statistics")
    
    title = user_id.username

    total_skills_value = (
                        user_skills.abstraction + 
                        user_skills.decomposition + 
                        user_skills.algorithms + 
                        user_skills.generalization + 
                        user_skills.evaluation
                        )

    return render(request, 'personal_stats.html', {
                                                    "skill": user_skills,
                                                    "performance": user_performance,
                                                    "total": total_skills_value,
                                                    "year": year,
                                                    "title": title
                                                    })

@login_required()
@user_passes_test(views.check_not, login_url= '/home/')
def all_stats(request): 
    title = 'Estadísticas generales de los estudiantes'
    year = date.today().year
    
    code = request.user.user_profile_set.get().access_code 
    students = User_Profile.objects.filter(access_code=code, user_role=True)

    skills = [0,0,0,0,0]
    total_skills_value = 0
    performance = [0,0,0,0,0,0,0,0,0,0,0,0]


    for i in range(len(students)):
        try:
           skills[0] += students[i].user.my_skills_set.get().abstraction
           skills[1] += students[i].user.my_skills_set.get().decomposition
           skills[2] += students[i].user.my_skills_set.get().algorithms
           skills[3] += students[i].user.my_skills_set.get().generalization
           skills[4] += students[i].user.my_skills_set.get().evaluation
                        
           performance[0] += students[i].user.my_performance_set.get().january
           performance[1] += students[i].user.my_performance_set.get().february
           performance[2] += students[i].user.my_performance_set.get().march
           performance[3] += students[i].user.my_performance_set.get().april
           performance[4] += students[i].user.my_performance_set.get().may
           performance[5] += students[i].user.my_performance_set.get().june
           performance[6] += students[i].user.my_performance_set.get().july
           performance[7] += students[i].user.my_performance_set.get().august
           performance[8] += students[i].user.my_performance_set.get().september
           performance[9] += students[i].user.my_performance_set.get().october
           performance[10] += students[i].user.my_performance_set.get().november
           performance[11] += students[i].user.my_performance_set.get().december        
        except:
            pass

    for t in skills:
        total_skills_value += t

    search = request.GET.get("search")
    
    if search:
            students =  User_Profile.objects.filter(access_code=code, 
                                                    user_role=True, 
                                                    user_id__email__icontains = search)

    return render(request, 'all_stats.html',{
                                            "students": students,
                                            "skill": skills,
                                            "performance": performance,
                                            "total": total_skills_value,
                                            "year": year, 
                                            "title": title
                                            })


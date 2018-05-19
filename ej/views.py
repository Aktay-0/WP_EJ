from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .JournalStorage import *

# Create your views here.

def sortGroup(group):
    for i in range(0, len(group)):
        for j in range(0, len(group) - 1):
            if group[j].course > group[j + 1].course:
                buffer = group[j]
                group[j] = group[j + 1]
                group[j + 1] = buffer
    return group

def index(request):
    if request.method == "POST":
        try:
            usr = Users_login.objects.get(login = request.POST['log'])
            if usr.check_password(request.POST['pas']):
                request.session[request.META['REMOTE_ADDR']] = usr.login
                if usr.user_type == 'teacher':
                    return redirect('teacher_info')
                elif usr.user_type == 'admin':
                    return redirect('admin_info')
                elif usr.user_type == 'student':
                    return redirect('student_info')
        except:
            return render(request, 'ej/login.html/login.html', { })

    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Users_login.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        if usr.user_type == "teacher":
            return redirect('teacher_info')
        elif usr.user_type == "admin":
            return redirect('admin_info')
        elif usr.user_type == "student":
            return redirect('student_info')
    else:
        return render(request, 'ej/login.html/login.html', { })

 #   return render(request, 'ej/login.html/login.html', { })

def logout(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        del request.session[request.META['REMOTE_ADDR']]
        return redirect('index')
    else:
        return redirect('index')
###########################--Teacher--#############################
def teacher_log(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Users_login.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        return render(request, 'ej/teacher.html/log.html/log.html', {'usr': usr})
    else:
        return redirect('index')

def teacher_module(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Teachers.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        storage = JournalPage("")
        if request.method == 'POST':
            module = Journals.objects.get(group_code = request.POST['group'])
            subjects = module.subjects.split(';')

            if request.POST['month'] == '0' and module.september != None:
                storage = JournalPage(module.september)
            elif request.POST['month'] == '1' and module.october != None:
                storage = JournalPage(module.october)
            elif request.POST['month'] == '2' and module.november != None:
                storage = JournalPage(module.november)
            elif request.POST['month'] == '3' and module.december != None:
                storage = JournalPage(module.december)
            elif request.POST['month'] == '4' and module.january != None:
                storage = JournalPage(module.january)
            elif request.POST['month'] == '5' and module.february != None:
                storage = JournalPage(module.february)
            elif request.POST['month'] == '6' and module.march != None:
                storage = JournalPage(module.march)
            elif request.POST['month'] == '7' and module.april != None:
                storage = JournalPage(module.april)
            elif request.POST['month'] == '8' and module.may != None:
                storage = JournalPage(module.may)
            elif request.POST['month'] == '9' and module.june:
                storage = JournalPage(module.june)
            else:
                storage = JournalPage("")
            return render(request, 'ej/teacher.html/module.html/module.html', {'usr': usr, 'subjects': subjects, 'storage':storage, 'month': request.POST['month'], 'group': request.POST['group']})
        else:
            return redirect('teacher_group')
    else:
        return redirect('index')

def teacher_logbook(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        if request.method == 'POST':
            usr = Users_login.objects.get(login = request.session[request.META['REMOTE_ADDR']])
            return render(request, 'ej/teacher.html/logbook.html/logbook.html', {'usr': usr})
        else:
            return redirect('teacher_group')
    else:
        return redirect('index')

def teacher_schedule_teacher(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Teachers.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        schedule = Schedule.objects.all()
        return render(request, 'ej/teacher.html/schedule_teacher.html/schedule_teacher.html', {'usr': usr, 'shedule': schedule})
    else:
        return redirect('index')

def teacher_table(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Users_login.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        return render(request, 'ej/teacher.html/table.html/table.html', {'usr': usr})
    else:
        return redirect('index')

def teacher_load(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Users_login.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        return render(request, 'ej/teacher.html/load.html/load.html', {'usr': usr})
    else:
        return redirect('index')

def teacher_group(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Teachers.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        groups = Groups.objects.all()
        groups = sortGroup(groups)

        courses = []
        courses.append(groups[0].course)
        for i in groups:
            if i.course != courses[len(courses) - 1]:
                courses.append(i.course)

        return render(request, 'ej/teacher.html/group.html/group.html', {'usr': usr, 'groups': groups, 'courses': courses})
    else:
        return redirect('index')

def teacher_curator(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Teachers.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        try:
            ivents = Ivents.objects.get(teacher = request.session[request.META['REMOTE_ADDR']])
            return render(request, 'ej/teacher.html/curator.html/curator.html', {'usr': usr, 'ivents': ivents})
        except:
            return redirect('teacher_info')
    else:
        return redirect('index')

def teacher_info(request):
    if request.session.get(request.META['REMOTE_ADDR'], '') != '':
        usr = Users_login.objects.get(login = request.session[request.META['REMOTE_ADDR']])
        return render(request, 'ej/teacher.html/info.html/info.html', {'usr': usr})
    else:
        return redirect('index')
###########################--Teacher--#############################

###########################--Edit_Journal--########################
def edit_journal(request):
    return HttpResponse("OK")
###########################--Edit_Journal--########################

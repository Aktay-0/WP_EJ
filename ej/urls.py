from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'logout$', views.logout, name='logout'),
    url(r'teacher/log$', views.teacher_log, name='teacher_log'),
    url(r'teacher/module$', views.teacher_module, name='teacher_module'),
    url(r'teacher/logbook$', views.teacher_logbook, name='teacher_logbook'),
    url(r'teacher/schedule_teacher$', views.teacher_schedule_teacher, name='teacher_schedule_teacher'),
    url(r'teacher/table$', views.teacher_table, name='teacher_table'),
    url(r'teacher/load$', views.teacher_load, name='teacher_load'),
    url(r'teacher/group$', views.teacher_group, name='teacher_group'),
    url(r'teacher/curator$', views.teacher_curator, name='teacher_curator'),
    url(r'teacher/info$', views.teacher_info, name='teacher_info'),
    url(r'edit/journal$', views.edit_journal, name='edit_journal'),
]

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Users_login)
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Admins)
admin.site.register(Groups)
admin.site.register(Subjects)
admin.site.register(Schedule)
admin.site.register(Replacements)
admin.site.register(Journals)
admin.site.register(Ivents)
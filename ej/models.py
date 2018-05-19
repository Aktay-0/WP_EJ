from django.db import models

# Create your models here.

class Users_login(models.Model):
    login = models.CharField(max_length = 15, blank = True, primary_key = True)
    password = models.CharField(max_length = 15, blank = True)
    user_type = models.CharField(max_length = 10, blank = True)

    def check_password(self, password):
        if (self.password == password) :
            return True
        else:
            return False

class Students(models.Model):
    login = models.ForeignKey('Users_login', on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 15, blank = True)
    last_name = models.CharField(max_length = 15, blank = True)
    patronymic = models.CharField(max_length = 15, blank = True)
    birth_date = models.DateTimeField(blank = True)
    group = models.ForeignKey('Groups', on_delete = models.CASCADE, blank = True, null = True)

class Teachers(models.Model):
    login = models.ForeignKey('Users_login', on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 15, blank = True)
    last_name = models.CharField(max_length = 15, blank = True)
    patronymic = models.CharField(max_length = 15, blank = True)
    supervised_group = models.ForeignKey('Groups', on_delete = models.CASCADE, blank = True, null = True)

class Admins(models.Model):
    login = models.ForeignKey('Users_login', on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 15, blank = True)
    last_name = models.CharField(max_length = 15, blank = True)
    patronymic = models.CharField(max_length = 15, blank = True)

class Groups(models.Model):
    group_code = models.CharField(max_length = 10, primary_key = True, blank = True)
    name = models.CharField(max_length = 10, blank = True)
    profession = models.CharField(max_length = 30, blank = True)
    course = models.IntegerField(blank = True)
    sub_number = models.IntegerField(blank = True)

class Subjects(models.Model):
    subject_code = models.CharField(max_length = 10, blank = True, primary_key = True)
    subject_name = models.CharField(max_length = 50, blank = True)
    pm_module = models.CharField(max_length = 10, blank = True)

class Schedule(models.Model):
    week = models.IntegerField(blank = True)
    day = models.CharField(max_length = 15, blank = True)
    group = models.ForeignKey('Groups', on_delete = models.CASCADE, blank = True, null = True)
    learnings = models.TextField(blank = True)

class Replacements(models.Model):
    date = models.DateTimeField(blank = True)
    week = models.IntegerField(blank = True)
    number_learn = models.IntegerField(blank = True)
    group = models.ForeignKey('Groups', on_delete = models.CASCADE, blank = True, null = True)
    learn = models.ForeignKey('Subjects', on_delete = models.CASCADE, blank = True, null = True)
    teacher = models.ForeignKey('Teachers', on_delete = models.CASCADE, blank = True, null = True)
    custom_learn = models.CharField(max_length = 30, blank = True)
    custom_teacher = models.CharField(max_length = 30 , blank = True)
    classroom = models.CharField(max_length = 5, blank = True)

class Journals(models.Model):
    #id_journal = models.AutoField()
    group_code = models.ForeignKey('Groups', on_delete = models.CASCADE, blank = True, null = True)
    subjects = models.TextField(blank = True)
    september = models.TextField(blank = True)
    october = models.TextField(blank = True)
    november = models.TextField(blank = True)
    december = models.TextField(blank = True)
    january = models.TextField(blank = True)
    february = models.TextField(blank = True)
    march = models.TextField(blank = True)
    april = models.TextField(blank = True)
    may = models.TextField(blank = True)
    june = models.TextField(blank = True)
    year = models.TextField(blank = True)

class Ivents(models.Model):
    teacher = models.ForeignKey('Teachers', on_delete = models.CASCADE, blank = True, null = True)
    date = models.CharField(max_length = 30 , blank = True)
    name = models.CharField(max_length = 30 , blank = True)
    info = models.TextField(blank = True)

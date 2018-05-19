
class Mark():
    date = ""
    mark = ""

    def __init__(self, date, mark):
        self.unpackage(date, mark)

    def unpackage(self, date, mark):
        self.date = date
        self.mark = mark

    def package(self):
        return self.date + "&" + self.mark

    def clear(self):
        self.date = ""
        self.mark = ""

class Student():
    name = ""
    marks = []

    def __init__(self, name, marks):
        self.unpackage(name, marks)

    def unpackage(self, name, marks):
        buffer = []
        self.name = name

        for i in marks:
            if i != "":
                mark = i.split('&')
                buffer.append(Mark(mark[0], mark[1]))
        
        self.marks = buffer.copy()

    def package(self):
        mark = ""
        for i in self.marks:
            mark += i.package() + "$"
        return self.name + "/" + mark

    def addMark(self, date, mark):
        self.marks.append(Mark(date, mark))

    def removeMark(self, date, mark):
        for i in range(len(self.marks) - 1):
            if self.marks[i].date == date and self.marks[i].mark == mark:
                del self.marks[i]

class Lesson():
    date = ""
    hours = ""
    theme = ""
    task = ""

    def __init__(self, date, hours, theme, task):
        self.unpackage(date, hours, theme, task)

    def unpackage(self, date, hours, theme, task):
        self.date = date
        self.hours = hours
        self.theme = theme
        self.task = task

    def package(self):
        return self.date + "&" + self.hours + "&" + self.theme + "&" + self.task

    def clear(self):
        self.date = ""
        self.hours = ""
        self.theme = ""
        self.task = ""


class Subject():
    name = ""
    students = []
    lessons = []

    def __init__(self, name, students, lessons):
        self.unpackage(name, students, lessons)

    def unpackage(self, name, students, lessons):
        buffer = []
        self.name = name
        for i in students:
            if i != "":
                student = i.split('/')
                buffer.append(Student(student[0], student[1].split('$')))
        
        self.students = buffer.copy()
        buffer = []

        for i in lessons:
            if i != "":
                lesson = i.split('&')
                buffer.append(Lesson(lesson[0], lesson[1], lesson[2], lesson[3]))
            
        self.lessons = buffer.copy()

    def package(self):
        student = ""
        lesson = ""
        for i in self.students:
            student += i.package() + "+"
        for i in self.lessons:
            lesson += i.package() + "+"
        return self.name + ":" + student + "|" + lesson

    def addMark(self, student, date, mark):
        for i in self.students:
            if i.name == student:
                i.addMark(date, mark)

    def addLesson(self, date, hours, theme, task):
        self.lessons.append(Lesson(date, hours, theme, task))

    def addStudent(self, student):
        self.students.append(Student(student, ""))

    def removeMark(self, student, date, mark):
        for i in self.students:
            if i.name == student:
                i.removeMark(date, mark)

    def removeLesson(self, date, hours, theme, task):
        for i in range(len(self.lessons) - 1):
            if self.lessons[i].date == date and self.lessons[i].hours == hours and self.lessons[i].theme == theme and self.lessons[i].task == task:
                del self.lessons[i]

    def removeStudent(self, student):
        for i in range(len(self.students)):
            if self.students[i].name == student:
                del self.students[i]
    def getMarks(self, student):
        for i in self.students:
            if i.name == student:
                return i.marks
            return None

class JournalPage():
    subjects = []

    def __init__(self, page):
        self.unpackage(page)

    def unpackage(self, page):
        buffer = []
        subject = page.split('#')

        for i in subject:
            if i != "":
                sub = i.split(':')
                buff = sub[1].split('|')
                students = buff[0].split('+')
                lessons = buff[1].split('+')
                buffer.append(Subject(sub[0], students, lessons))
        
        self.subjects = buffer.copy()

    def package(self):
        subject = ""

        for i in self.subjects:
            if i.name != "":
                subject += i.package() + "#"
        return subject

    def addMark(self, subject, student, date, mark):
        for i in self.subjects:
            if i.name == subject:
                i.addMark(student, date, mark)
    
    def addLesson(self, subject, date, hours, theme, task):
        for i in self.subjects:
            if i.name == subject:
                i.addLesson(date, hours, theme, task)

    def addStudent(self, subject, student):
        for i in self.subjects:
            if i.name == subject:
                i.addStudent(student)

    def addSubject(self, subject):
        self.subjects.append(Subject(subject, "", ""))

    def removeMark(self, subject, student, date, mark):
        for i in self.subjects:
            if i.name == subject:
                i.removeMark(student, date, mark)
    
    def removeLesson(self, subject, date, hours, theme, task):
        for i in self.subjects:
            if i.name == subject:
                i.removeLesson(date, hours, theme, task)     

    def removeStudent(self, subject, student):
        for i in self.subjects:
            if i.name == subject:
                i.removeStudent(student)   

    def removeSubject(self, subject):
        for i in range(len(self.subjects) - 1):
            if self.subjects[i].name == subject:
                del self.subjects[i]

    def getMarks(self, subject, student):
        for i in self.subjects:
            if i.name == subject:
                return i.getMarks(student)
                
    def getLessons(self, subject):
        for i in self.subjects:
            if i.name == subject:
                return i.lessons
        return None

    def getSubjects(self):
        return self.subjects

    

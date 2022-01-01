from django.contrib import admin
from .models import Employee,School,Teacher,Courses,CourseTeacher,Links,Notes,Test,Questions,Answer
# Register your models here.
admin.site.register(Employee)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(CourseTeacher)
admin.site.register(Links)
admin.site.register(Notes)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(Questions)
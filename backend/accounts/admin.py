from django.contrib import admin
from .models import User, Official, Student, Teacher, Staff

admin.site.register(User)
admin.site.register(Official)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Staff)

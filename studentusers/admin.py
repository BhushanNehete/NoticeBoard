from django.contrib import admin
from .models import Student


# Register your models here.
class StudentsUser(admin.ModelAdmin):
    list_display = ['id', 'roll_no', 'div', 'department']


admin.site.register(Student, StudentsUser)

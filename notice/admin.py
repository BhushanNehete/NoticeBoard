from django.contrib import admin
from .models import Notice, Department


# Register your models here.
class NtcAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'notice_department', 'created']


admin.site.register(Notice, NtcAdmin)


class DeptAdmin(admin.ModelAdmin):
    list_display = ['id', 'department']


admin.site.register(Department, DeptAdmin)

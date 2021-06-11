from django.forms import ModelForm
from .models import Notice, Department, ContactUs


class addNotice(ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'image', 'notice_department']
        # labels = {'notice_department': 'Notice Department'}


class addDepartment(ModelForm):
    class Meta:
        model = Department
        fields = ['id', 'department']


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['phone', 'message']

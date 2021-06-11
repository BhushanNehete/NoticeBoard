from django.shortcuts import render, redirect
from .models import Notice, Department, ContactUs
from .forms import addNotice, addDepartment, ContactUsForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from studentusers.models import Student


# Create your views here.
@login_required()
def home(request):
    all_dept = Department.objects.all()
    dept = request.GET.get('dept')
    if dept is None:
        ntc = Notice.objects.all().order_by('-created')
    else:
        ntc = Notice.objects.filter(notice_department=dept).order_by('-created')

    return render(request, "notice/home.html", {'notice': ntc, 'all_dept': all_dept})


@staff_member_required
def add(request):
    if request.method == 'POST':
        form = addNotice(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Notice Added")
            return redirect('home')
    else:
        form = addNotice()
    return render(request, "notice/add.html", {"form": form})


@staff_member_required
def add_dept(request):
    if request.method == 'POST':
        form = addDepartment(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department Added")
            return redirect('home')
    else:
        form = addDepartment()
    return render(request, "notice/dept.html", {"form": form})


@staff_member_required
def delete(request, id):
    if request.method == "POST":
        ntc = Notice.objects.get(pk=id)
        ntc.delete()
        messages.success(request, "Notice Deleted")
        return HttpResponseRedirect("/")


@staff_member_required
def update(request, id):
    if request.method == "POST":
        ntc = Notice.objects.get(pk=id)
        form = addNotice(request.POST, request.FILES, instance=ntc)
        if form.is_valid():
            form.save()
            messages.success(request, "Notice Updated")
            return redirect("/")
    else:
        ntc = Notice.objects.get(pk=id)
        form = addNotice(instance=ntc)
    return render(request, "notice/update.html", {"form": form})


def contactUs(request):
    contact = None
    if request.user.is_staff:
        contact = ContactUs.objects.all().order_by('-id')
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.first_name = request.user.first_name
            obj.last_name = request.user.last_name
            obj.Email = request.user.email
            obj.save()
            return redirect('home')
    else:
        form = ContactUsForm()
    return render(request, "notice/contact.html", {"form": form, "contact": contact})

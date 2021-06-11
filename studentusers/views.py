from django.shortcuts import render, redirect
from .forms import CreateUser, StudentUser
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student


# Create your views here.

def register(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        sform = StudentUser(request.POST)

        if form.is_valid() and sform.is_valid():
            user = form.save()
            std = sform.save(commit=False)
            std.user = user
            std.save()

            messages.success(request, "Registered Successfully")
            return redirect("login")
    else:
        form = CreateUser()
        sform = StudentUser()
    return render(request, "studentusers/register.html", {"form": form, "sform": sform})


def students(request):
    if request.user.is_staff is True:
        user = User.objects.exclude(is_staff=True)

    return render(request, "studentusers/students.html", {"users": user})

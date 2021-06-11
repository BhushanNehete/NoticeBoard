from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("dept/", views.add_dept, name="dept"),
    path("delete/<int:id>", views.delete, name="delete_ntc"),
    path("<int:id>", views.update, name="update"),
    path("contact/", views.contactUs, name="contact"),
]
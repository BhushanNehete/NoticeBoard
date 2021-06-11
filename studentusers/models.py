from django.db import models
from django.contrib.auth.models import User
import notice.models as nm


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    div = models.CharField(max_length=5)
    department = models.ForeignKey(nm.Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


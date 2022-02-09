from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12, null=True, blank=True)
    major = models.CharField(max_length=30, default="Undeclared")
    college = models.CharField(max_length=30, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

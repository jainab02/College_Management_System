from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Course(models.Model):

    Cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)


class Department(models.Model):
    Did  = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length = 50)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Sid = models.AutoField(primary_key=True)
    student_name= models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    phone = models.CharField(max_length = 10)
    course=  models.ForeignKey(Course,on_delete = models.CASCADE)
    current_sem =  models.IntegerField()
    passing_year = models.CharField(max_length = 10)
    Did= models.ForeignKey(Department,on_delete = models.CASCADE)


class Faculty(models.Model):
    Fid = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department,on_delete = models.CASCADE)

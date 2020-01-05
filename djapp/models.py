from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class RegistrationData(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    User_Name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Mobile=models.BigIntegerField()
    Email_id=models.EmailField()

class feedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=50)
    feedback=models.CharField(max_length=500)
class contactData(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    COURSES_CHOICES=(
        ('Python','PYTHON'),
        ('Django','DJANGO'),
        ('Rest Api','REST API'),
        ('Mysql','MYSQL')
    )
    courses=MultiSelectField(max_length=300,choices=COURSES_CHOICES)
    TRAINER_CHOICES=(
        ('Ravi','RAVI'),
        ('Sai','SAI'),
        ('Hari','HARI')
    )
    trainer = MultiSelectField(max_length=300, choices=TRAINER_CHOICES)
    BRANCHES_CHOICES=(
        ('Hyd','HYDERABAD'),
        ('Pune','PUNE'),
        ('Chennai','CHENNAI')
    )
    branches=MultiSelectField(max_length=300,choices=BRANCHES_CHOICES)
    date=models.DateField(max_length=100)
    gender=models.CharField(max_length=100)
class coursesData(models.Model):
    course_no=models.IntegerField()
    course_name=models.CharField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_exp=models.CharField(max_length=50)
from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class company(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=42, default="")
    address = models.CharField(max_length=500)
    company_name = models.CharField(max_length=150, default="")
    phone = models.CharField(max_length=20)
    company_phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Inactive")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "company"


class applicants(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=42,default="")
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20,default="")
    area = models.CharField(max_length=150,default="")
    marital_status = models.CharField(max_length=20,default="Unmarried")
    qualification = models.CharField(max_length=200,default="")
    experience = models.CharField(max_length=100,default="")
    present_company = models.CharField(max_length=150,default="")
    current_salary = models.CharField(max_length=20,default="")
    expected_salary = models.CharField(max_length=20,default="")
    job_location = models.CharField(max_length=200,default="")
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "applicants"

class job(models.Model):
    email= models.EmailField()
    company_name = models.CharField(max_length=400, default="")
    job_tittle= models.CharField(max_length=400, default="")
    location = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)
    salary = models.CharField(max_length=500)
    requirement = models.CharField(max_length=500)
    applicants = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "job"

class application(models.Model):
    stu_email= models.EmailField()
    job_id = models.IntegerField()
    stu_name = models.CharField(max_length=400, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "application"

class resume_list(models.Model):
    stu_email =models.EmailField()
    resume = models.FileField(upload_to='upload/')

    class Meta:
        db_table = "resume_list"
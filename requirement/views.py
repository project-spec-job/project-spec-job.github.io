from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
# Create your views here.

@csrf_exempt
def index(request):
    toy = job.objects.all()
    context = {
        'toys': toy
    }
    return render(request, 'index.html',context)
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        if applicants.objects.filter(email=email).exists():
            m = applicants.objects.get(email=email)
            if m.password == request.POST['pass']:
                request.session['email'] = email
                request.session['name'] = m.name
                return redirect('/')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    else:
        return render(request, 'login.html')



def resume(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if request.session.get('email', None):
            email = request.session['email']
            re = resume_list(stu_email=email, resume=myfile)
            re.save()
            return redirect('/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'resume.html')


def reviews(request):
    return render(request, 'reviews.html')
def find_salary(request):
    return render(request, 'find_salary.html')



def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        if applicants.objects.filter(email=email).exists():
            return redirect("/registration")
        else:
            user = applicants(email=email,password=password)
            user.save();
        if user:
            request.session['email'] = email
            return redirect("registration2")
        else:
            return redirect("registration")

    else:
        return render(request, 'registration.html')

def registration2(request):
    if request.method == 'POST':
        toy =  applicants.objects.get(email=request.session['email'])
        toy.name = request.POST['name']
        toy.dob = request.POST['dob']
        toy.gender = request.POST['gender']
        toy.area= request.POST['area']
        toy.martial_status = request.POST['ms']
        toy.qualification = request.POST['qui']
        toy.experience = request.POST['exp']
        toy.current_salary= request.POST['cs']
        toy.expected_salary = request.POST['es']
        toy.phone = request.POST['phone']
        toy.job_location = request.POST['location']
        toy.present_company = request.POST['company']
        request.session['name'] = toy.name
        toy.save()
        return redirect('/')
    else:
        return render(request, 'regsitration2.html')


def employee(request):
    if request.method == 'POST':
        email = request.POST['email']
        if company.objects.filter(email=email).exists():
            m = company.objects.get(email=email)
            if m.password == request.POST['pass']:
                request.session['c_email'] = email
                request.session['c_name'] = m.name
                return redirect('post_a_job')
            else:
                return redirect('/employee')
        else:
            return redirect('/employee')
    else:
        return render(request, 'employee.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def company_signup(request):
    if request.method == 'POST':
        name =request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        address = request.POST['address']
        phone = request.POST['phone']
        cname = request.POST['cname']
        c_phone = request.POST['c_phone']

        if company.objects.filter(email=email).exists():
            return redirect("/employee")
        else:
            user = company(name=name,email=email, password=password,phone=phone,address=address,company_name=cname,company_phone=c_phone)
            user.save();
        if user:
            request.session['c_email'] = email
            request.session['c_name']= cname
            return redirect("post_a_job")
        else:
            return redirect("company_signup")

    else:
        return render(request, 'companysignup.html')


def post_a_job(request):
    if request.method == 'POST':
        cname = request.POST['company']
        email = request.session['c_email']
        job_title = request.POST['job']
        location = request.POST['location']
        experience = request.POST['experience']
        requirement = request.POST['requirement']
        salary = request.POST['salary']

        user = job(company_name=cname, email=email, job_tittle=job_title, location=location, experience=experience, salary=salary, requirement=requirement,list=[""])
        user.save();
        if user:
            return redirect("view_all_jobs")
        else:
            return redirect("post_a_job")

    else:
        return render(request, 'post a job.html')


def view_all_jobs(request):
    toy = job.objects.filter(email = request.session['c_email'])
    context = {
        'toys': toy
    }
    return render(request,  'view all jobs.html',context)


def edit_job(request, id):
    toy = job.objects.get(pk=id)
    context = {
        'toys': toy
    }
    return render(request, 'edit_job.html', context)


def delete_job(request, id):
    toys = job.objects.get(pk=id)
    toys.delete()
    return redirect('/view_all_jobs')


def update(request, id):
    toy = job.objects.get(pk=id)
    toy.company_name = request.GET['company']
    toy.job_tittle = request.GET['job']
    toy.location = request.GET['location']
    toy.experience= request.GET['experience']
    toy.salary = request.GET['salary']
    toy.requirement = request.GET['requirement']
    toy.save()
    return redirect('/view_all_jobs')


def apply_job(request,id):
    toy = job.objects.get(pk=id)
    toy.applicants=toy.applicants+1
    toy.save()
    email = request.session['email']
    name = request.session['name']
    data = application(stu_email=email,job_id=id,stu_name=name)
    data.save()
    return redirect('/')


def search(request):
    if request.method == 'POST':
        s2 = request.POST['c_name']
        s1 = request.POST['city']
        if job.objects.filter(job_tittle=s2).exists():
            toy = job.objects.filter(Q(job_tittle=s2)| Q(location=s1))
            context = {
                'toys': toy
            }
            return render(request, 'search.html', context)
        else:
            return render(request, 'no_result.html')
    else:
        return render(request, 'search.html')


def view_job(request, id):
    toy = job.objects.get(pk=id)
    if application.objects.filter(job_id= toy.id).filter(stu_name = request.session['name']).exists():
        context = {
            'toys': toy,
            'toy2': False
        }
    else:
        context = {
            'toys': toy
        }
    return render(request, 'view_job.html', context)


def view_applicant(request,id):
    toy2 = application.objects.filter(job_id=id)
    context = {
        'toys': toy2
    }
    return render(request, 'view_applicant.html', context)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('registration2', views.registration2, name='registration2'),
    path('post_a_job', views.post_a_job, name='post_a_job'),
    path('view_all_jobs', views.view_all_jobs, name='view_all_jobs'),
    path('edit_job/<id>/',views.edit_job, name='edit_job'),
    path('delete_job/<id>/',views.delete_job, name='delete_job'),
    path('employee', views.employee, name='employee'),
    path('company_signup', views.company_signup, name='company_signup'),
    path('find_salary', views.find_salary, name='find_salary'),
    path('resume', views.resume, name='resume'),
    path('reviews', views.reviews, name='reviews'),
    path('update/<id>/', views.update, name='update' ),
    path('apply_job/<id>/', views.apply_job, name='apply_job' ),
    path('search', views.search, name='search' ),
    path('view_job/<id>/', views.view_job, name='view_job' ),
    path('view_applicant/<id>/', views.view_applicant, name='view_applicant' ),

   ]

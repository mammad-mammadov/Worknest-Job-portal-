from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='jobs/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='job_list'), name='logout'),
path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
path('post-job/', views.post_job, name='post_job'),
path('company-dashboard/', views.company_dashboard, name='company_dashboard'),
path('save-job/<int:job_id>/', views.save_job, name='save_job'),
path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
]


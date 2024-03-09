from django.urls import path
from .import views
from job.views import ShowPosts
urlpatterns = [
    
    path('register/', views.EmpRegister.as_view(), name='employer_register'),
    path('login/',views.EmployerLogin.as_view(), name='employer_login'),
    path('logout/',views.Emplogout, name='employer_logout'),
    path('employer_profile/', views.EmpProfileView.as_view(), name= 'employer_profile'),
    path('jobs/', views.EmpJobView.as_view(), name= 'show_job_employer'),
    path('show_posts/', ShowPosts.as_view(), name= 'show_posts'),
    path('filter_job/<int:id>', views.JobFilter, name='filter_job'),
]

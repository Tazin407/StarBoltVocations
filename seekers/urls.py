from django.urls import path
from .import views
urlpatterns = [
    path('seeker_register/', views.SeekerRegister.as_view(), name='seeker_register'),
    path('seeker_login/', views.SeekerLogin.as_view(), name='seeker_login'),
    path('seeker_profile/', views.ProfileView.as_view(), name="seeker_profile"),
    path('jobs/', views.SeekerJobView.as_view(), name="show_job_seeker"),
   path('filter_job/<int:id>', views.JobFilter, name='filter_job_seeker'),
]

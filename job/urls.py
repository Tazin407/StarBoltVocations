from django.urls import path
from .import views

urlpatterns = [
   path('add_job/', views.JobFormView.as_view(), name='add_job'),
   path('job_details/<int:id>', views.JobDetails.as_view(), name='job_details'),
   path('filter_job/<int:id>', views.JobFilter, name='filter_job'),
   path('apply_job/<int:id>', views.ApplyJob, name='apply_job'),
   path('cancel_application/<int:id>', views.CancelApplication, name='cancel_application'),
   
]

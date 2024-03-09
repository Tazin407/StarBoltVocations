from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, View,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib import messages
from .import forms 
from .import models
from employers.models import Employer
from seekers.models import Seeker
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

class JobFormView(CreateView, LoginRequiredMixin):
    template_name='job_form.html'
    form_class= forms.JobForm
    success_url= reverse_lazy('employer_profile')
    
    def form_valid(self, form):
        emp= models.Employer.objects.get(user= self.request.user)
        form.instance.employer = emp
        print(form)
        messages.success(self.request, 'Created a posting successfully')
        return super().form_valid(form)
    
class JobView(ListView):
    model= models.Job
    template_name="all_jobs.html"
    
    def get_queryset(self) :
        queryset= models.Job.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        category= models.Category.objects.all()
        
            
        context['category']=  category
        return context
    
    
def JobFilter(request, id):
    category= models.Category.objects.get(id=id)
    jobs= models.Job.objects.filter(category= category)
    all_category= models.Category.objects.all()
    print(jobs)
    
    return render(request, 'all_jobs.html', {'job_list':jobs,'category': all_category})

class JobDetails(DetailView):
    model= models.Job
    pk_url_kwarg='id'
    template_name= 'job_details.html'
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            
            try:
                employer= Employer.objects.get(user= self.request.user)
                context['type']='employer'
                self.template_name = 'job_details_employer.html'

            except Employer.DoesNotExist:
                
                try:
                    seeker= Seeker.objects.get(user= self.request.user)
                    context['type']= 'seeker'
                    self.template_name = 'job_details_seeker.html'
                    try :
                        apply= models.ApplyJob.objects.get(candidate= seeker, job__id=self.kwargs[self.pk_url_kwarg])
                        context['applied']= True
                        
                    except models.ApplyJob.DoesNotExist:
                        context['applied'] = False
                        
                    
                except Seeker.DoesNotExist:
                    context['type']= 'none'
                   
            
        return context
    
    
def ApplyJob(request, id):
    job= models.Job.objects.get(id=id)
    seeker= Seeker.objects.get(user= request.user)
    
    if request.method== 'POST':
        form= forms.ApplyJobForm(request.POST, request.FILES)
        print('hello')
        
        if form.is_valid():
            print('Yay')
            form.instance.job= job
            form.instance.candidate= seeker
            form.save()
            messages.success(request, f'Sent Application Successfully')
            
            # to_email= job.employer.user.email
            
            # mail_subject="A new Application"
            # message= render_to_string('new_application.html',{'job': job.title})
            # send_email= EmailMultiAlternatives(mail_subject,'', to=[request.user.email] )
            # send_email.attach_alternative(message, 'text/html')
            # send_email.attach(model_cv.cv.name, model_cv.cv.read(), model_cv.cv.file.content_type)
            # send_email.send()
            return redirect('job_details', id)
      
    form= forms.ApplyJobForm()
    return render(request, 'apply_job.html',{'form': form, 'job': job})     

def CancelApplication(request, id):
    seeker= Seeker.objects.get(user= request.user)
    job= models.Job.objects.get(id= id)
    apply= models.ApplyJob.objects.get(candidate= seeker, job=job)
    apply.delete()
    
    mail_subject="Transaction Message"
    message= render_to_string('cancel_application.html',{'job': job.title})
    send_email= EmailMultiAlternatives(mail_subject,'', to=[request.user.email] )
    send_email.attach_alternative(message, 'text/html')
    send_email.send()
    
    return redirect('job_details', id)
    
    
    
    
    
    
    

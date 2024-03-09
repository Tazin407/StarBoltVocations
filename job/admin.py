from django.contrib import admin
from django.db import models
from .import models
# Register your models here.

admin.site.register(models.Category)

class JobAdmin(admin.ModelAdmin):
    list_display=['title','category','status']
    
admin.site.register(models.Job, JobAdmin)
admin.site.register(models.ApplyJob)

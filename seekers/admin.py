from django.contrib import admin
from .import models
# Register your models here.

class SeekersAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','education_level','skillset','experience']
    
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(models.Seeker, SeekersAdmin)
admin.site.register(models.SeekerPersonal)

from django.contrib import admin
from .models import worker, machine,prise
# Register your models here.

class worker_admin (admin.ModelAdmin):
    #fields = ['category','title','slug','image','image_small','text','published_date']
    list_display = ['name','phone','department']
    list_filter = ['id','department']


class prise_admin (admin.ModelAdmin):
    list_display = ['name','prise_item','category','size']
    list_editable =['name','prise_item','size']
    list_filter = ['id','category']



# class machine_admin (admin.ModelAdmin):
#     #fields = ['category','title','slug','image','image_small','text','published_date']
#     list_display = ['name','phone','department']
#     list_filter = ['id','department']

admin.site.register(worker,worker_admin)
admin.site.register(machine)
admin.site.register(prise,prise_admin)
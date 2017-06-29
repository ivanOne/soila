from django.contrib import admin
from .models import Category, Post
# Register your models here.

# Модель Категории в Админке
class CategoryAdmin (admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title', )}




class PlaceAdmin (admin.ModelAdmin):
    fields = ['category','title','slug','image','image_small','text','published_date']
    list_display = ['title','category']
    list_filter = ['id','category','published_date']
    prepopulated_fields = {'slug':('title', ),
                           'image_small':('image', )}

admin.site.register(Post,PlaceAdmin)
admin.site.register(Category,CategoryAdmin)
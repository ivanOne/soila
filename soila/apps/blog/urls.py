from django.conf.urls import url,include
from . import views


urlpatterns = [

    url(r'^category/(?P<slug_category>[-\w]+)/$', views.post_list_by_category, name="post_list_by_category"),
    url(r'(?P<slug>[-\w]+)/$', views.post_detail, name ="post_detail"),
    #url(r'(?P<slug_category>[-\w]+)/$', views.post_list, name="post_list"),
    url(r'', views.post_list, name= 'post_list' ),


]

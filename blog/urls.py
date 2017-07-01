from django.conf.urls import url,include
from .views import CategoryPostList, post_detail, post_list, post_list_by_category


urlpatterns = [

    url(r'^category/(?P<slug_category>[-\w]+)/$', CategoryPostList.as_view(), name="post_list_by_category"),
    url(r'(?P<slug>[-\w]+)/$', post_detail, name ="post_detail"),
    #url(r'(?P<slug_category>[-\w]+)/$', views.post_list, name="post_list"),
    url(r'', post_list, name= 'post_list' ),


]

from django.shortcuts import render_to_response, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def post_list_by_category(request, slug_category):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-published_date')
    if slug_category:
        category = get_object_or_404(Category, slug=slug_category)
        posts = posts.filter(category=category)
    args = {}
    args['posts'] = posts
    args['category'] = category
    args['categories'] = categories
    args['recent_posts'] = posts[0:3]

    return render_to_response('post_list_by_category.html', args)


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    categories = Category.objects.all()
    args={}
    args['posts']=posts
    args['categories'] = categories
    args['recent_posts']=posts[0:3]

    return render_to_response('post_list.html', args)





def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    all_posts = Post.objects.all()
    recent_posts = reversed(all_posts[0:1])

    return render_to_response('post_detail.html', {'post':post,'categories':categories, 'recent_posts':recent_posts})
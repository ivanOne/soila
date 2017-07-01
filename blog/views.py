from django.shortcuts import render_to_response, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
#Простой, но одновремено некрасивый способ описывать view с пагинацией
def post_list_by_category(request, slug_category):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug_category)
    posts = Post.objects.filter(category=category).order_by('-published_date')
    recent_posts = posts[0:3]

    #Готовим пагинатор, закидываем в него посты, и определяем по сколько записей выводить
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        #Нормальная работа пагинатора закидываем страницу получаем результат
        posts = paginator.page(page)
    except PageNotAnInteger:
        #в гет попапа какая то хрень, показываем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        #Например страниц у нас 10 а кто то решил запросить 11ю шлем ему последнюю страницу
        posts = paginator.page(paginator.num_pages)

    args = dict()
    args['posts'] = posts
    args['category'] = category
    args['categories'] = categories
    args['recent_posts'] = recent_posts
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
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


# Create your views here.
# def index(request):
#     template = 'posts/index.html'
#     title = 'Это главная страница проекта Yatube'
#     context = {
#         # В словарь можно передать переменную
#         'title': title
        
#     }
#     return render(request, template, context)
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    context = {
        # В словарь можно передать переменную
        'group': group,
        'posts': posts,
      
    }
    return render(request, 'posts/group_list.html', context)
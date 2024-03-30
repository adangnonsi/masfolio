
from django.shortcuts import get_object_or_404, render

from .models import Blog, Category

# Create your views here.


def blog(request,category_slug=None):
    blogs=Blog.objects.all()
    categories=Category.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        blogs=Blog.objects.filter(categorie=category)
    return render(request,'blog/blog.html',{'categories':categories, 'blogs':blogs})


def blog_detail(request, my_id):
     blogs=Blog.objects.get(id=my_id) 
     categories=Category.objects.all() 
     
     
     return render(request,'blog/blog-single.html',{ 'blogs':blogs,'categories':categories})

from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
    b=Blog.objects.all()
    return render(request,'blog/all_blogs.html',{'b':b})


def detail(request,blog_id):
    bvar=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'bvar':bvar})

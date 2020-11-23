from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.


def all_blogs(request):
    blog = Blog.objects.order_by('-Pub_date')

    return render(request, 'blog/all_blog.html', {'blog': blog})


def detail(request,blog_id):
     blog_detail=get_object_or_404(Blog,pk=blog_id)
     return render(request,'blog/detail.html',{'blog_detail':blog_detail})
from django.shortcuts import render
from .models import Blogs
# Create your views here.
def home(requests):
    context = {
        'blogs':Blogs.objects.all()
    }
    return render(requests,'base.html',context = context)
def read_blog(requests,blog_name):

    blog = Blogs.objects.get(title=blog_name)
    print(blog)
    blog_list = []
    for blogs in Blogs.objects.all():
        if blogs.title == blog_name:
            continue
        else:
            blog_list.append(blogs)

    context = {
        'title':blog.title,
        'content':blog.content,
        'author':blog.author,
        'date_posted':blog.date_posted,
        'image':blog.image,
        'bloglist':blog_list,
        # 'blogs':Blogs.objects.all()
    }
    return render(requests,'read_blog.html',context = context)
def privacy_policy(requests):
    return render(requests,'privacy_policy.html',context={})
from django.shortcuts import render
from .models import Post 

# Create your views here.

def new(request):
    return render(request,'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    post = Post(title=title, content=content)
    post.save()
    return render(request,'create.html')
    
def index(request):
    #all post
    posts= Post.objects.all()
    return render(request, 'index.html',{'posts':posts})
# def throw
# def catch
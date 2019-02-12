from django.shortcuts import render,redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def new(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        #DB INSERT
        post = Post(title=title, content=content, image=image)
        post.save()
        
        return redirect('posts:detail', post.pk)
        #create
    else:
        return render(request,'new.html')


    
def index(request):
    #all post
    posts= Post.objects.all()
    return render(request, 'index.html',{'posts':posts})
# def throw
# def catch

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html',{'post':post})
    
# def naver(request, q):
    
#     return redirect(f'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={q}')
    
def delete(request, post_id):
    if request.method == 'POST':
    #삭제코드
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
    else:
        return render(request,'delete.html')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        #update
        
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('posts:detail',post.pk)
    else:
        return render(request, 'edit.html', {'post':post})
    

   
    
def comments_create(request, post_id):
    # 댓글을 달 게시물
    post = Post.objects.get(pk=post_id)
    
    #form에서 넘어온 댓글 내용
    content= request.POST.get('content')
    
    #댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    
    return redirect('posts:detail', post.pk)
    
def comments_delete(request, post_id, comment_id):
    comment=Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)
    
    
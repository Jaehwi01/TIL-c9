from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
    
# 정리
# class Post :  django - model /  db - table
# post = Post() :   django - instance (or) object / db - record or row
# title :   django - field / db - column


#방법1
# post = Post(title='hello-1')
# post.save()
# post -> 출력

#방법2
# post2= Post.objects.create(title='hello-2')
# post2 -> 출력     (이경우 create에서 save까지 됨)
#방법3
# post3 = Post()
# post3.title = 'hello-3'
# post3.save()
# post3 -> 출력

# 2.READ

# 2-1. ALL
# posts= Post.objects.all()

# 2-2 One
# 방법 1 
# Post.objects.get(id=1)  or  Post.objects.get(pk=1) or  Post.objects.get(title='hello-1') <- 타이틀 정확히 일치
# 방법2
# from django.shortcuts import get_object_or_404
# post = get_object_or_404(Post, pk=1) # id=1,  title='hello-1' 로도 가능
# 방법3
# post = Post.objects.filter(pk=1)[0] # id=1 , title='hello-1'로도 가능
# post = Post.objects.filter(pk=1).first()

# 2-3 where(filter)
# posts = Post.objects.filter(title='hello-1')
# post = Post.objects.filter(title='hello-1').first() # 또는 [0]

# like
# posts = Post.objects.filter(title__contains='lo')  언더바 2개

# order_by
# posts = Post.objects.order_by('title') # 제목 오름차순
# posts = Post.objects.order_by('-title') #제목 내림차순 

# offset & limit
# post = Post.objects.all()[0]  -> offset 0 limit 1
# post = Post.objects.all()[1]  -> offset 1 limit 1
# post = Post.objects.all()[1:3] -> offset 1 limit 2
# post = Post.objects.all()[offset : offset + limit]

# 3. update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save() # 실제 db저장

# 4. delete
# post = Post.objects.get(pk=1)
# post.delete()
# 한줄로
# Post.objects.get(pk=1).delete()
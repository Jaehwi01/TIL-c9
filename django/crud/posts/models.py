from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    
# 1. Create
# post = post(title='hello',content='world')
# post.save()

# 2. Read
# 2.1. All
# posts = Post.objects.all()
# 2.2 Get one
# post = Post.objects.get(pk=1) 
# 2.3 filter (Where)
# posts = Post.objets.filter(title='Hello').all()
# post = Post.objets.filter(title='Hello').first()
# 2.4 LIKE
# posts = Post.objucts.filter(title__contains='He').all()
# 2.5 order_by(정렬)
# posts = Post.object.order_by('title').all()   # 오름차순
# posts = Post.object.order_by('-title').all()  # 내림차순
# 2.6 limit & offset
# [offset:offset-limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post= Post.objects.get(pk=2)
# post.delete()

# 4. Uodate
# post = Post.objects.get(pk=1)
# post.title = 'hi'
# post.save()        #hello -> hi

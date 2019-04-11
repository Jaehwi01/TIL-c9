from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
# Create your models here.


def post_image_path(instance, filename):
    return f'posts/{instance.pk}/{filename}'  # or {filename} == {instance.content}.jpeg
class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content=models.TextField()
    # image=models.ImageField(blank=True)
    image=ProcessedImageField(
                upload_to=post_image_path, #저장위치
                processors=[ResizeToFill(600,600)], #처리할 작업 목록
                format = 'JPEG', #저장포맷
                options={'quality':90}, #옵션
        )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
                    
class comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#첫번쨰인자는 어떠한 것이랑 관계를 할건지.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content= models.TextField()
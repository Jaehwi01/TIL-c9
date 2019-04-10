from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data=models.DateTimeField('datepublished')
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASECADE)
    choice_tex = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
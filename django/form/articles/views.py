from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article=form.save()
            # title = form.cleaned_data.get('title')  #< ModelForm 일땐 ['title']로?
            # content = form.cleaned_data.get('content')        
            # article = Article(title=title, content=content)
            # article.save()
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm()
        
    return render(request, 'form.html', {'form':form})
        
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article)
        
    return render(request, 'form.html', {'form':form})    
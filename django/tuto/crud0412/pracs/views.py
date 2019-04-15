from django.shortcuts import render
from . import views
from .models import Prac
# Create your views here.
def list(request):
    posts=Prac.objects.all()
    return render(request,'list.html')
    
def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        audience = request.POST.get('audience')
        return redirect('pracs:detail',post.pk)
    return

def delete(request):
    return
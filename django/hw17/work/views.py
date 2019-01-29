from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def new(request):
    return render(request,'new.html')
    
def index(request):
    
    work= Student.objects.all()
    
    return render(request,'index.html',{'work':work})
    
def create(request):
    name = request.POST.get('name')
    age =request.POST.get('age')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    
    work = Student(name=name, age=age, birthday=birthday, email=email)
    work.save()
    
    return redirect(f'/work/{work.pk}/')
    
def detail(request, work_id):
    work= Student.objects.get(pk=work_id)
    return render(request, 'detail.html',{'work':work})
    
# def create():
def delete(request, work_id):
    work = Student.objects.get(pk=work_id)
    work.delete()
    return redirect('/work/')
    
def edit(request, work_id):
    work = Student.objects.get(pk=work_id)
    return render(request, 'edit.html', {'work':work})
    
def update(request, work_id):
    work=Student.objects.get(pk=work_id)
    work.name=request.POST.get('name')
    work.age=request.POST.get('age')
    work.birthday=request.POST.get('birthday')
    work.email=request.POST.get('email')
    work.save()
    return redirect(f'/work/{work_id}/')
    

from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request,'info.html')
    
def student(request, name):
    return render(request,'student.html', {'name':name})
from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('name')
    content = request.POST.get('content')
    
    s = Students(title=title, content=content)
    s.save()
    
    return redirect(f'/Students/{s.pk}/')    
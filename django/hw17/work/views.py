from django.shortcuts import render
from .models import Work

# Create your views here.
def index(render):
    work=Work.objects.all()
    return render(request,'index.html',{'work':work})
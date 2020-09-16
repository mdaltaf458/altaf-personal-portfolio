from django.shortcuts import render
from .models import Project
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    projects= Project.objects.all()

    return render(request,'portfolio/home.html',{'projects':projects})

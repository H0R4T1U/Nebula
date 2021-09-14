from django.shortcuts import render

from .models import Project
# Create your views here.
def index(request):
    projects = Project.objects.all().order_by('-stars')[:4]
    context = {
        'projects':projects
    }
    return render(request,'Nebula/index.html',context)
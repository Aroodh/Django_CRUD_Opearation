from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    completed_tasks=Task.objects.filter(is_completed=True)
    
    context={
        'tasks':task,
        'complted_tasks':completed_tasks
    }
    return render(request,'home.html',context)
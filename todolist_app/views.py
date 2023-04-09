from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from todolist_app.forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request,'New task added!')
        return redirect('todolist')
    else:    
        all_tasks = TaskList.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        
        return render(request,"todolist.html",{'all_tasks':all_tasks})

@login_required
def contact(request):
    context = {
        'welcome_text':"Welcome To Contact Page"
    }
    return render(request,"contact.html",context)


def index(request):
    context = {
        'index_text':"Welcome To Index Page"
    }
    return render(request,"index.html",context)


def aboutus(request):
    context = {
        'welcome_text':"Welcome To About Page"
    }
    return render(request,"aboutus.html",context)

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request,'Access restricted, you are not allowed!')
    return redirect('todolist')

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,'Access restricted, you are not allowed!')
    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('Task Edited!'))
        return redirect('todolist')
    else:    
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request,"edit.html",{'task_obj':task_obj})


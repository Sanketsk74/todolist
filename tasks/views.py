from django.shortcuts import render,redirect


from django.http import HttpResponse

from . models import Task

from . forms import TaskForm

# Create your views here.

def index(request):
    form = TaskForm()
    tasks = Task.objects.all()  

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'tasks.html',
    {'tasks':tasks,'form':form})


def updateTask(request,pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context ={'form':form}

    return render(request,'update_task.html',context)

def deleteTask(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {'task':task}
    
    return render(request,'delete_task.html',context)
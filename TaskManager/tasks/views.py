from django.shortcuts import render, redirect
from .models import Task

def index_view(request):
    return render(request, 'index.html')

def create_view(request):

    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        poster = request.FILES.get('poster')

        task_obj = Task(title=title, description=description, status=status, poster=poster)
        task_obj.save()
        print("saved")
        return redirect('list')

    return render(request, 'add.html')

def list_view(request):
    tasks = Task.objects.all()
    context = {'tasks' : tasks}
    return render(request, 'list.html', context)

def edit_view(request, task_id):
    print("editng...."+str(task_id))
    task_obj = Task.objects.get(id=task_id)
    context = {'task_obj':task_obj}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        if len(request.FILES) > 0:
            poster = request.FILES.get('poster')
            task_obj.poster=poster
        task_obj.title=title
        task_obj.description=description
        task_obj.status=status
        task_obj.save()
        print("Edited")
        return redirect('list')
        
    return render(request, 'edit.html', context)

def delete_view(request, task_id):
    print("deleting...."+str(task_id))
    task_obj = Task.objects.get(id=task_id)
    task_obj.delete()
    return redirect('list')

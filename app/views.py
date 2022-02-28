from django.shortcuts import render,redirect,get_object_or_404
from  . models import Task
# Create your views here.
def home(request):
    success = False
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        success = True
    return render(request, 'index.html',{"success":success})
def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    print(allTasks[0].taskTitle)
    return render(request, 'tasks.html',context)
def update(request, id):
    task = Task.objects.get(id=id)
    context = {
        "id":task.id,
        "title": task.taskTitle,
        "desc": task.taskDesc
    }

    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        Task.objects.filter(id=id).update(taskTitle=title, taskDesc=desc)

        return redirect("/tasks")
    return render(request, 'edit.html',context)

def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()  
    return redirect("/tasks") 

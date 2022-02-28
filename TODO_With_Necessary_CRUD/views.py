from django.shortcuts import render,redirect
from .models import Task,Task_list,Custem,Tags
# Create your views here.
def home(request):
    obj=Task.objects.all()
    list_data=Task_list.objects.all()
    list_custem=Custem.objects.all()
    list_tags=Tags.objects.all()
    return render(request,'index.html',{'data':obj,'list':list_data,'custem':list_custem , 'tags':list_tags})

def load_task(request):
    return render(request,'Task.html')

def insert_task(request):
    if request.method=='POST':
        vname=request.POST.get('task')
        obj=Task()
        obj.task_name=vname
        obj.save()
        return redirect('/')
    else:
        return render(request, 'Task.html')

def editTask(request,tid):
    obj=Task.objects.get(id=tid)
    return render(request,'EditTask.html',{'task':obj})

def updateTask(request,tid):
    obj = Task.objects.get(id=tid)
    vname=request.POST.get('task')
    obj.task_name=vname
    obj.save()
    return redirect('/')

def deleteTask(request,tid):
    obj = Task.objects.get(id=tid)
    obj.delete()
    return redirect('/')

def load_list(request):
    return  render(request,'List.html')
def insertListTask(request):
    if request.method=='POST':
        vlist=request.POST.get('list')
        obj=Task_list()
        obj.task_list=vlist
        obj.save()
        return redirect('/')
    else:
        return render(request, 'List.html')
def editList(request,lid):
    obj=Task_list.objects.get(id=lid)
    return render(request,'EditTask_List.html',{'list':obj})
def updateList(request,lid):
    obj = Task_list.objects.get(id=lid)
    vname=request.POST.get('list')
    obj.task_list=vname
    obj.save()
    return redirect('/')
def deleteTaskList(request,tid):
    obj = Task_list.objects.get(id=tid)
    obj.delete()
    return redirect('/')


def load_custem(request):
    return  render(request,'custem.html')

def insert_custem(request):
    if request.method=='POST':
        vcustem=request.POST.get('custem')
        obj=Custem()
        obj.custem=vcustem
        obj.save()
        return redirect('/')
    else:
        return render(request, 'custem.html')
def editcustom(request,cid):
    obj=Custem.objects.get(id=cid)
    return render(request,'Editcustem.html',{'custem':obj})


def updatecustem(request,cid):
    obj = Custem.objects.get(id=cid)
    vcustem=request.POST.get('custem')
    obj.custem_name=vcustem
    obj.save()
    return redirect('/')


def deletecustem(request,tid):
    obj = Custem.objects.get(id=tid)
    obj.delete()
    return redirect('/')



def load_tags(request):
    return render(request,'tags.html')

def insert_tags(request):
    if request.method=='POST':
        vtags=request.POST.get('tags')
        obj=Tags()
        obj.tags=vtags
        obj.save()
        return redirect('/')
    else:
        return render(request, 'tags.html')


def edittags(request,gid):
    obj=Tags.objects.get(id=gid)
    return render(request,'Edittags.html',{'tags':obj})

def updatetags(request,gid):
    obj = Tags.objects.get(id=gid)
    vtags=request.POST.get('tags')
    obj.tags_name=vtags
    obj.save()
    return redirect('/')

def deletetags(request,tid):
    obj = Tags.objects.get(id=tid)
    obj.delete()
    return redirect('/')
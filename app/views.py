from datetime import datetime
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import AddTask
from django.contrib import messages


def home(request):
    if request.method == "GET":
        add_form = AddTask()
        if 'toDoUser' in request.COOKIES:
            usr = request.COOKIES['toDoUser']
            data = Todo.objects.filter(user_id = usr,is_done = False)
            return render(request=request , template_name="view.html",context = {'data':data,'add_form':add_form})
        else:
            user = Users.objects.create()
            
            response = render(request,"view.html",context= {'user':user,'add_form':add_form}) 
            response.set_cookie('toDoUser',user)   
            return response


    return render(request,"index.html")
    
def add_task(request):
    form_data = AddTask(request.POST)  
    if form_data.is_valid():
        title = form_data.cleaned_data['title']
        body = form_data.cleaned_data['body']
        due = form_data.cleaned_data['due_date']
        usr_id = Users.objects.get(id = request.COOKIES['toDoUser'])

        Todo.objects.create(title=title,body=body,due_date=due,user_id = usr_id)

        messages.success(request,"Task added succesfully .")
        
    return redirect("home")


def del_task(request,tid):

    curr_user_id = request.COOKIES['toDoUser']
    
    curr_user_obj = Users.objects.get(id = curr_user_id)
    
    deleting_task = Todo.objects.get(id = tid)
    
    if deleting_task.user_id == curr_user_obj:
        deleting_task.delete()
        messages.success(request,"Task deleted successfully !")

    return redirect('home')

def edit_task(request,tid):

    editing_task = Todo.objects.get(id = tid)

    title= request.POST['title']
    body = request.POST['body']
    due_date = request.POST['due_date']

    curr_user_id = request.COOKIES['toDoUser']
    
    curr_user_obj = Users.objects.get(id = curr_user_id)

    if editing_task.user_id == curr_user_obj:
        Todo.objects.filter(id = tid).update(title=title , body = body , due_date = due_date)
        messages.success(request,"Task edited successfully !")

    return redirect("home")    

def complete(request,tid):

    completing_task = Todo.objects.get(id = tid)

    curr_user_id = request.COOKIES['toDoUser']
    
    curr_user_obj = Users.objects.get(id = curr_user_id)

    completed_date = datetime.now()
    

    if completing_task.user_id == curr_user_obj:
        Todo.objects.filter(id = tid).update(is_done = True,completed_on = completed_date)

        messages.success(request,"Task completed successfully !")

    return redirect("home") 

def view_completed(request):

    curr_user_id = request.COOKIES['toDoUser']


    compl_tasks = Todo.objects.all().filter(user_id = curr_user_id,is_done = True)

    return render(request,"completed.html",context= {"data": compl_tasks})       



    








    
    
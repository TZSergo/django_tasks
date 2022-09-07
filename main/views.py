from django.shortcuts import render
from .models import Task
from django.views.generic import DetailView, UpdateView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# class taskUpdate(UpdateView):
#     model = Task
#     template_name = 'main/index.html'
#     fields = ['title', 'task']


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("login")


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        tasks = Task.objects.all()
        return render(request, 'main/index.html', {'title':'Главная страница', 'tasks':tasks})

    #if request.user.is_authenticated:
    #tasks = Task.objects.all()
    #return render(request, 'main/index.html', {'title':'Главная страница', 'tasks':tasks})
    #else:
        #return render(request, 'main/index.html', {'title':'Не авторизаван!', 'tasks':''})
        #return redirect('%s?login%s' % (settings.LOGIN_URL, request.path))

    


def getData(request):
    tasks = Task.objects.all
    return render(request, 'main/tasktable.html', {'title':'Главная страница', 'tasks':tasks})


def taskDetal(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'main/task_detale.html', {'title':f'Task: {pk}', 'task':task})


def sortTable(request):
    action = request.POST.get('action')
    if action == 'title':
        task = Task.objects.order_by('title')
    elif action == 'task':
        task = Task.objects.order_by('task')
    return render(request, 'main/tasktable.html', {'title':'Главная страница', 'tasks':task})


def uocData(request):
    if request.POST.get('act') == 'update':
        title = request.POST.get('title')
        task = request.POST.get('task')
        task_id = request.POST.get('task_id')
        Task.objects.filter(pk=task_id).update(title=title)
        Task.objects.filter(pk=task_id).update(task=task)
        tasks = Task.objects.all()
        return render(request, 'main/tasktable.html', {'tasks':tasks})

    elif request.POST.get('act') == 'create':
        title = request.POST.get('title')
        task = request.POST.get('task')
        author_fn = request.POST.get('author_fn')
        author_ln = request.POST.get('author_ln')
        Task.objects.create(title=title, 
                            task=task, 
                            author_fn=author_fn, 
                            author_ln=author_ln
                            )
        #p = Task(title=title, task=task)
        #p.save(force_insert=True)
        tasks = Task.objects.all()
        return render(request, 'main/tasktable.html', {'tasks':tasks})

    elif request.POST.get('act') == 'delete':
        task_id = request.POST.get('task_id')
        Task.objects.filter(pk=task_id).delete()
        tasks = Task.objects.all()
        return render(request, 'main/tasktable.html', {'tasks':tasks})

# def index(request):
#     return HttpResponse('<h3>Hello</h3>')

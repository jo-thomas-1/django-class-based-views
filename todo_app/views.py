from django.shortcuts import render
from . models import Task
from . forms import TaskForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('todo_app:class_based_detail_view', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('todo_app:class_based_list_view')

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']

        task = Task(name=name, priority=priority, date=date)
        task.save()

        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'delete.html', {'task': task})

def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'form': form, 'task': task})
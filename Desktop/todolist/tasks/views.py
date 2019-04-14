from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Tasks
from django.urls import reverse,reverse_lazy
# Create your views here.
#def home(request):
#    return render(request,'tasks/home.html')
class IndexView(generic.ListView):
    template_name = 'tasks/home.html'
    context_object_name = 'all_tasks'
    def get_queryset(self):
        return Tasks.objects.all()
class DetailView(generic.DetailView):
    template_name = 'tasks/detail.html'
    model = Tasks
    context_object_name = 'task'
class CreateTask(generic.CreateView):
    template_name = 'tasks/forms_template.html'
    model = Tasks
    fields = ['TaskName','Description','DueDate','priority']
class UpdateTask(generic.UpdateView):
    template_name = 'tasks/forms_template.html'
    model = Tasks
    fields = ['TaskName','Description','DueDate','priority']
class DeleteTask(generic.DeleteView):
    model = Tasks
    success_url = reverse_lazy('tasks:homepage')

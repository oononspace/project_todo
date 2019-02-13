from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskCreateForm
from .models import Task

class IndexView(generic.ListView):
    model = Task
    paginate_by = 6

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('taskapp:index')

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('taskapp:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('taskapp:index')

class DetailView(generic.DetailView):
    model = Task

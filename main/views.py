# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

# def home(request):
# 	return render(request, 'index.html')


class HomePage(ListView):
	model = Task
	template_name = 'index.html'
	context_object_name = 'tasks'
	ordering = ['completed', '-date_created']


class TaskDetailView(DetailView):
	model = Task
	template_name = 'task_detail.html'
	context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	template_name = 'task_create.html'
	fields = ['title', 'overview']
	success_url = reverse_lazy('home')

	# set user to task automatically
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class TaskUpdateView(UpdateView):
	model = Task
	template_name = 'task_update.html'
	fields = ['title', 'overview', 'completed']
	success_url = reverse_lazy('home')


class TaskDeleteView(DeleteView):
	model = Task
	template_name = 'task_delete.html'
	success_url = reverse_lazy('home')
	context_object_name = 'task'
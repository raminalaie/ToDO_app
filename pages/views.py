from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import TaskUpdateForm
from django.views import View
from django.shortcuts import redirect


class HomePageView(LoginRequiredMixin, ListView):
    template_name = "home.html"
    context_object_name = "post"
    form_class = Post

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("home")
    form_class = TaskUpdateForm
    template_name = "pages/update_task.html"


class TaskComplete(LoginRequiredMixin, View):
    model = Post
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        object = Post.objects.get(id=kwargs.get("pk"))
        if Post.objects.filter(id=kwargs.get("pk"), status=False):
            object.status = True
            object.save()
            return redirect(self.success_url)
        elif Post.objects.filter(id=kwargs.get("pk"), status=True):
            object.status = False
            object.save()
            return redirect(self.success_url)


class PostDelete (LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "pages/post_delete.html"
    success_url = reverse_lazy("home")




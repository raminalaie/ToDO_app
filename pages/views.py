from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from .models import Post
from django.urls import reverse_lazy


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

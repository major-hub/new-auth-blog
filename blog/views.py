from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import New


class HomeListView(ListView):
    model = New
    template_name = 'blog/home.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class UserNewsView(ListView):
    model = New
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return New.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super(UserNewsView, self).get_context_data(**kwargs)
        context['title'] = f"Все статы от ползователя { self.kwargs.get('username') }"
        return context


class PostDetailView(DetailView):
    model = New
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = New.objects.get(pk=self.kwargs.get('pk'))
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = New
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = New
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        new = self.get_object()
        return True if self.request.user == new.author else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = New
    success_url = reverse_lazy('blog:home')
    # template_name = 'blog/new_confirm_delete.html'

    def test_func(self):
        new = self.get_object()
        return True if self.request.user == new.author else False


def contact(request):
    return render(request, 'blog/contact.html')

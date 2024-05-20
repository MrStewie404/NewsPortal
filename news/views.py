# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from .filters import PostFilter
from .models import Post
from .forms import PostForm


class PostsList(ListView):
    raise_exception = True
    queryset = Post.objects.order_by('datetime')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class SearchList(ListView):
    queryset = Post.objects.order_by('datetime')
    template_name = 'search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    


def search(request):
    news_list = Post.objects.all()
    news_filter = PostFilter(request.GET, queryset=news_list)
    return render(request, 'news/search.html', {'filter': news_filter})


class WhatCreate(DetailView):
    model = Post
    # context_object_name = 'news'
    template_name = 'create.html'



class PostDetail(DetailView):
    model = Post
    context_object_name = 'news'
    template_name = 'news_id.html'

class NewsCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.content_type = 'NW'
        return super().form_valid(form)
    
class ArticleCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.content_type = 'AR'
        return super().form_valid(form)

class PostEdit(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')
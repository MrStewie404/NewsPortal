# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.shortcuts import render
from .filters import PostFilter
from .models import Post
from .forms import PostForm


class PostsList(ListView):
    queryset = Post.objects.order_by('datetime')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news'


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


def page(request):
    page = request.GET.get('page')
    html = f"<html><body>{page}</body></html>"

    return HttpResponse(html)



class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, PostCategory
from datetime import datetime

# Create your views here.

class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'show_post.html'
    context_object_name = 'show_post'




from django.shortcuts import render,get_object_or_404
from account.models import User
from django.views.generic import ListView,DetailView
from . import models
from account import mixins

class Articlelist(ListView):
    queryset = models.Article.objects.published().order_by('-date')
    paginate_by = 2

class Detail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(models.Article.objects.published(),slug=slug)
        return article

class Preview(mixins.AuthorAccessMixin,DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        article = get_object_or_404(models.Article,pk=pk)
        return article

class Category(ListView):
    template_name = 'blog/category_list.html'
    paginate_by = 2
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(models.Category.objects.active(),slug=slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

class Author(ListView):
    template_name = 'blog/author_list.html'
    paginate_by = 2
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
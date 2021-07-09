from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.contrib.auth.views import LoginView,PasswordChangeView
from blog import models
from django.urls import reverse_lazy
from .models import User
from . import mixins,forms

class ArticleList(mixins.AuthorsAccessMixin,ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Article.objects.all().order_by('-date')
        else:
            return models.Article.objects.filter(author=self.request.user).order_by('-date')

class ArticleCreate(mixins.AuthorsAccessMixin,mixins.FieldsMixin,mixins.FormMixin,CreateView):
    model = models.Article
    template_name = 'registration/article-create-update.html'

class ArticleUpdate(mixins.AuthorAccessMixin,mixins.FieldsMixin,mixins.FormMixin,UpdateView):
    model = models.Article
    template_name = 'registration/article-create-update.html'

class ArticleDelete(mixins.SuperUserAccessMixin,DeleteView):
    model = models.Article
    success_url = reverse_lazy("account:home")
    template_name = 'registration/article-delete.html'

class Profile(UpdateView):
    model = User
    success_url = reverse_lazy("account:profile")
    form_class = forms.ProfileForm
    template_name = 'registration/profile.html'

    def get_object(self):
        return User.objects.filter(pk = self.request.user.pk).first()
    
    def get_form_kwargs(self):
        kwargs = super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
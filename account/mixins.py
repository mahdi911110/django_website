from django.shortcuts import redirect, render,get_object_or_404
from blog import models

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['header','span','title','slug','category','body','time','image','status','is_special']
        if request.user.is_superuser:
            self.fields.append('author')
        return super().dispatch(request, *args, **kwargs)

class FormMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status == 'i':
                self.obj.status = 'd'
        return super().form_valid(form)

class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(models.Article,pk=pk)
        if article.author == request.user and article.status in ['d','b'] or request.user.is_superuser:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            return render(request,'registration/access_denied.html')

class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")
        else:
            return redirect("account:login")

class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request,'registration/access_denied.html')
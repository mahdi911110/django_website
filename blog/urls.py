from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.Articlelist.as_view(), name='list'),
    path('page/<int:page>', views.Articlelist.as_view(), name='list'),
    path('article/<slug>', views.Detail.as_view(), name='detail'),
    path('preview/<int:pk>', views.Preview.as_view(), name='preview'),
    path('category/<slug>', views.Category.as_view(), name='category'),
    path('category/<slug>/page/<int:page>', views.Category.as_view(), name='category'),
    path('author/<slug:username>', views.Author.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', views.Author.as_view(), name='author'),
]
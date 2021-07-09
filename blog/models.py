from django.db import models
from account.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class Category(models.Model):
    parent = models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children')
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30,unique=True)
    position = models.IntegerField()
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES = (
        ('p','publish'),
        ('d','draft'),
        ('i','investigation'),
        ('b','backed'),
    )
    header = models.CharField(max_length=40,default=None)
    span = models.CharField(max_length=50,default=None)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    category = models.ManyToManyField(Category,related_name='articles')
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg',blank=True,upload_to='image')
    is_special = models.BooleanField(default=False)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='articles')
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("account:home")

    def thumbnail(self):
        return format_html(f"<img width=100 style='border-radius: 5px;' src='{self.image.url}'>")
    thumbnail.short_description = 'image'

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])
    category_to_str.short_description = 'category'
    
    objects = ArticleManager()
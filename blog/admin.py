from django.contrib import admin
from . import models

def make_published(modeladmin,queryset,request):
    rows_update = queryset.update(status='p')
    if  rows_update == 1:
        message_bit = "1 story was draft "
    else:
        message_bit = "%s stories were draft" % rows_update
    modeladmin.get_message(request, "%s successfully marked as publish" % message_bit)
make_published.short_description = 'make published'

def make_draft(modeladmin,queryset,request):
    rows_update = queryset.update(status='d')
    if  rows_update == 1:
        message_bit = "1 story was published"
    else:
        message_bit = "%s stories were published" % rows_update
    modeladmin.get_message(request, "%s successfully marked as draft" % message_bit)
make_draft.short_description = 'make draft'

class CategoryDetail(admin.ModelAdmin):
    list_display = ('title','slug','position','parent','status')
    list_filter = (['status'])
    search_fields = ('title','slug','position')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(models.Category,CategoryDetail)

class ArticleDetail(admin.ModelAdmin):
    list_display = ('title','slug','date','update','category_to_str','thumbnail','is_special','author','status')
    list_filter = ('date','update','status','author')
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['date','update']
    actions = [make_published,make_draft]

admin.site.register(models.Article,ArticleDetail)
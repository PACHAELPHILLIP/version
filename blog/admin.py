from django.contrib import admin
from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','created','author',)
    prepopulated_fields = {'slug': ('title',),}
    
admin.site.register(Article, ArticleAdmin)

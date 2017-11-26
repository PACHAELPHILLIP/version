# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','created','author',)
    prepopulated_fields = {'slug': ('title',),}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Images)
admin.site.register(Comment)

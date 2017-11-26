from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# Create your models here.



class Article(models.Model):
    CATEGORY_CHOICES = (
    ('Tech', 'Tech'),    
    ('Review', 'Review'),
    ('Version', 'Version'),
    ('Music', 'Music'),
    ('Fashion', 'Fashion'),
    ('Culture', 'Culture'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True,default=None)
    source_logo= models.URLField(max_length=1000,null= True)
    sourcelink = models.URLField(max_length=1000 , null= True)
    thumbnail = models.URLField(max_length=1000)
    synopsis = models.TextField(max_length= 1000)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    body = RichTextField()
    video = models.BooleanField(default=False)
    tags = TaggableManager()
    created = models.DateField(null=True)
    author = models.ForeignKey(User,default=None)
    published = models.BooleanField(default=False)
    favorited_by_version = models.BooleanField(default = False)
    
   
    class Meta:
        verbose_name_plural = ('articles')
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

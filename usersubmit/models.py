from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import pre_save 
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField


# Create your models here.

class Post(models.Model):
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
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tags = TaggableManager()
    created = models.DateField(auto_now_add = True)
    author = models.ForeignKey(User, related_name='uploaded_by')
    published = models.BooleanField(default=True)
    allow_comments = models.BooleanField('allow comments', default=True)
    favorited_by_version = models.BooleanField(default = False)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='post_liked',
                                        blank=True)

    class Meta:
        verbose_name_plural = ('articles')
        ordering = ['-created']

    def __str__(self):
        return self.title

    

    def get_absolute_url(self):
        return reverse('usersubmit:postdetail', kwargs={'slug': self.slug})

    def get_first_image(self):
        return self.images_set.all()[0]

def create_slug(instance,new_slug=None):
    slug= slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs= Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists
    if exists():
        new_slug="%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug   

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)

pre_save.connect(pre_save_post_receiver,sender=Post)        
  
        

def get_image_filename(instance, filename):
    title = instance.article.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  



class Images(models.Model):
    article = models.ForeignKey(Post)
    image = ImageField(upload_to=get_image_filename,
                              verbose_name='Image', )
    body = models.TextField(max_length=500)    
    
    class Meta:
        verbose_name_plural = ('images')

       
    def __unicode__(self):
        return self.article                         



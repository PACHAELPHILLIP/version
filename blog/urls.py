from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.homeview, name='home'),
    url(r'^feeds/$', views.ArticleListView.as_view(), name='feeds'),
    url(r'^feeds/category/version/$', views.VersionListView.as_view(), name='versionlist'),
     url(r'^feeds/category/tech/$', views.TechListView.as_view(), name='Techlist'),
      url(r'^feeds/category/review/$', views.ReviewListView.as_view(), name='Reviewlist'),
    url(r'^feeds/category/music&entertainment/$', views.MusicListView.as_view(), name='Musiclist'),
     url(r'^feeds/category/lifestyle/$', views.LifestyleListView.as_view(), name='Lifestylelist'),   
    url(r'^feeds/tags/(?P<tag>\w+)$',views.tagpage ,name='tagepage'),
    url(r'^archive/$', views.ArchiveView.as_view(), name="archive"),
    url(r'search/$', views.search,name = 'search'),
    url(r'^feeds/(?P<slug>\S+)$', views.ArticleDetailView.as_view(), name='detail'),
   
]
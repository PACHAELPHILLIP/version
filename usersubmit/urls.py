from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'createpost/$', views.postview,name = 'createpost'),
     url(r'postfeeds/$', views.PostListView.as_view(),name = 'postfeeds'),
     url(r'^post_edit/(?P<slug>\S+)$', views.post_edit, name='postedit'),
     url(r'^remove/(?P<slug>\S+)/$', views.post_remove, name='post_remove'),
     url(r'^post/(?P<slug>\S+)$', views.ArticleDetailView.as_view(), name='postdetail'),
     url(r'^like/$', views.post_like, name='like'),
     
]

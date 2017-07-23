"""定义hardy_blogs的URL模式"""

from django.conf.urls import url
from . import views
from .views import ArticleDetailView, ArticlePublishView, ArticleEditView

urlpatterns = [
    url(r'^$', views.blog_index, name='blog_index'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    url(r'^article/(?P<title>\w+\.?\w+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),
]
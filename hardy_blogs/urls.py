"""定义hardy_blogs的URL模式"""

from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView, ArticlePublishView, ArticleEditView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='blog_index'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    url(r'^article/(?P<title>\w+\.?\w+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),
]
"""定义hardy_blogs的URL模式"""

from django.conf.urls import url
from .views import ArticleListView

urlpatterns = [
    # 主页
    url(r'^$', ArticleListView.as_view(), name='blog_index'),
]
"""定义hardy_blogs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.blog_index, name='blog_index'),
]
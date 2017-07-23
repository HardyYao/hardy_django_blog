from django.shortcuts import render
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.detail import DetailView
from .models import Article
from django.views.generic.edit import FormView
from hardy_blogs.forms import ArticlePublishForm
from django.core.urlresolvers import reverse

def blog_index(request):
    context = {
        'test': 'just for test',
        'welcome': 'hello world'
    }
    return render(request, 'blog_index.html', context)

class ArticlePublishView(FormView):
    template_name = 'article_publish.html'
    form_class = ArticlePublishForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(ArticlePublishView, self).form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'

    def get_object(self, **kwargs):
        title = self.kwargs.get('title')
        try:
            article = Article.objects.get(title=title)
            article.views += 1
            article.save()
            article.tags = article.tags.split()
        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        return article

class ArticleEditView(FormView):
    template_name = 'article_publish.html'
    form_class = ArticlePublishView
    article = None

    def get_initial(self, **kwargs):
        title = self.kwargs.get('title')
        try:
            self.article = Article.objects.get(title=title)
            initial = {
                'title': title,
                'content': self.article.content_md,
                'tags': self.article.tags,
            }
            return initial
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

    def form_invalid(self, form):
        form.save(self.request, self.article)
        return super(ArticleEditView, self).form_valid(form)

    def get_success_url(self):
        title = self.request.POST.get('title')
        success_url = reverse('article_detail', args=(title,))
        return success_url

class AdminRequiredMinin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AdminRequiredMinin, cls).as_view(**initkwargs)
        return staff_member_required(view)
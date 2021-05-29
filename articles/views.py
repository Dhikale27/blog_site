from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (UpdateView, DeleteView, CreateView)
from .models import Article, Comment
from django.urls import reverse_lazy
# Create your views here.


class ArticleListView(ListView):         # LoginRequiredMixin,
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):          # LoginRequiredMixin,
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'body', ]
    template_name = 'articles/article_edit.html'
    success_url = reverse_lazy('article_app:user_posts')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_app:user_posts')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title', 'body',)
    success_url = reverse_lazy('article_app:user_posts')

    '''
    >Below method is for taking by default author who is login.
    >In Artical class, 'author' field is necessary, otherwise we can not submit the form,
        so to fill that field we are going to use login user as author.
    >following method will grab the login user and fill the field of author by default.

    '''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def user_post_list(request):

    current_user = request.user

    posts = Article.objects.filter(author_id=current_user.id)

    return render(request, 'articles/user_post.html', {'posts': posts})


'''

    def get_context_data(self, **kwargs):
        self.country = get_object_or_404(Countries, id=self.kwargs['country_id'])
        kwargs['country'] = self.country
        return super().get_context_data(**kwargs)
'''


class AddCommentView(CreateView):
    model = Comment
    template_name = 'articles/add_coment.html'
    fields = ('name', 'email', 'body',)

    def form_valid(self, form):
        form.instance.article_id = self.request.article.id
        return super().form_valid(form)

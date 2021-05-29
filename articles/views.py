from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (UpdateView, DeleteView, CreateView)
from .models import Article, Comment
from django.urls import reverse_lazy
from .forms import ComentForm
# Create your views here.


class ArticleListView(ListView):         # LoginRequiredMixin,
    model = Article
    template_name = 'articles/article_list.html'


# class ArticleDetailView(DetailView):          # LoginRequiredMixin,
#     model = Article
#     template_name = 'articles/article_detail.html'


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


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk,)

    # comments = Article.comments.all()

    new_comment = None

    if request.method == 'POST':
        comment_form = ComentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_app:article_detail', pk=pk)

    else:
        comment_form = ComentForm()

    # 'comments': comments,
    return render(request, 'articles/article_detail.html', {'article': article, 'comment_form': comment_form, 'new_comment': new_comment})


def user_post_list(request):

    current_user = request.user

    posts = Article.objects.filter(author_id=current_user.id)

    return render(request, 'articles/user_post.html', {'posts': posts})


def user_article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk,)

    # # comments = Article.comments.all()

    # new_comment = None

    # if request.method == 'POST':
    #     comment_form = ComentForm(request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.article = article
    #         new_comment.save()
    #         return redirect('article_app:article_detail', pk=pk)

    # else:
    #     comment_form = ComentForm()

    # 'comments': comments,
    return render(request, 'articles/user_article_detail.html', {'article': article,})


# class AddCommentView(CreateView):
#     model = Comment
#     template_name = 'articles/add_coment.html'
#     fields = ('name', 'email', 'body',)

#     def form_valid(self, form):
#         form.instance.article_id = self.request.article.id
#         return super().form_valid(form)

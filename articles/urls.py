from django.urls import path
from .views import ArticleListView, article_detail, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, user_article_detail
from articles import views

app_name = 'article_app'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>/', article_detail, name='article_detail'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('user/article/', views.user_post_list, name='user_posts'),
    path('user/article/detail/<int:pk>/',
         user_article_detail, name='user_article_detail')  # 'user/article/detail/<int:pk>/' this path is imp, otherwise we will get 'article_detail'


]

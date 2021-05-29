from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    '''
    >Below class will order the posts according date of post

    '''
    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_app:article_detail', kwargs={'pk': self.pk})

# Crating Table for comments in our DATABASE


class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')

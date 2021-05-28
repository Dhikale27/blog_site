from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
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
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')

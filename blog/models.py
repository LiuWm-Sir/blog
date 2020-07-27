from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(u"博客标题", max_length=100)
    content = models.TextField(u"正文", blank=True, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.id])


from django.db import models
from blog.models import Article

class Comment(models.Model):
    title = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'

    )

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]



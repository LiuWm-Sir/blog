from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from comment.models import Comment
from blog.models import Article


def index(request):
    titles = Article.objects.all()
    return render(request, 'index.html', {"title": titles})


def article(request, id):
    titles = Article.objects.filter(pk=id)
    comments = Comment.objects.filter(title=id)


    return render(request, 'article.html', {"title": titles,'comments':comments})

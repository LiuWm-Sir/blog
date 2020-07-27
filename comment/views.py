from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from blog.models import Article
from .forms import CommentForm


def post_comment(request,titles_id):
    article = get_object_or_404(Article, id=titles_id)
    comment_form = CommentForm(request.POST)
    new_comment = comment_form.save(commit=False)
    new_comment.title = article
    new_comment.save()
    return redirect(article)




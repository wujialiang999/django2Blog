from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def article_detail(request,article_id):
    article = Article.objects.get(id=article_id)
    return HttpResponse("文章id为：{}，标题为:{},内容为:{}".format(article_id,article.title,article.content))
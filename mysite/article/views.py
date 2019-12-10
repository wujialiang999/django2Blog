from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def article_detail(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse("页面不存在!")
    return HttpResponse("文章id为：{},标题:{},内容:{}".format(article_id,article.title,article.content))
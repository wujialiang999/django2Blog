from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article
# Create your views here.

def article_detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    content={}
    content["article_obj"]=article
    return render(request,"article_detail.html",content)
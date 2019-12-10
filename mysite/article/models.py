from django.db import models
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30) #标题
    content = models.TextField()# 内容
    created_time=models.DateTimeField(auto_now_add=True)# 创建时间
    def __str__(self):
        return "Article:{}".format(self.title)
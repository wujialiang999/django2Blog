from django.contrib import admin

# Register your models here.
from .models import Article
# Register your models here.
# admin.site.register(Article)#注册模型
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=("id","title","content","created_time","last_update_time")
    ordering=("id",)#升序排列,倒叙加-,默认倒序
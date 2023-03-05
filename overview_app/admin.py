from django.contrib import admin
from .models import Contact, Article, ArticleList, TermsAndConditions


admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(ArticleList)
admin.site.register(TermsAndConditions)
from django.contrib import admin

from . models import ArticleCategory
from . models import Story
from . models import AuthorView
from . models import AuthorName

admin.site.register(ArticleCategory)
admin.site.register(Story)
admin.site.register(AuthorView)
admin.site.register(AuthorName)
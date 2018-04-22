from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # 自动将title的字段填充到slug
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    # 一个可以通过时间层快速导航的栏
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)


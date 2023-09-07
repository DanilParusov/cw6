from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name', 'content', 'data_creating', 'is_published',)
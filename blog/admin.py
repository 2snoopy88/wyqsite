from django.contrib import admin
from .models import Post,Category,Tag
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']


admin.site.register(Post,MarkdownxModelAdmin)
admin.site.register(Tag)
admin.site.register(Category)

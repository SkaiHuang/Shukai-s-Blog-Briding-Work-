from django.contrib import admin

from .models import Post, Comment, CV

class PostAdmin(admin.ModelAdmin):
    class Media: js = (
        'js/editor/kindeditor-all.js',
        'js/editor/config.js',
    )

class CVAdmin(admin.ModelAdmin):
    class Media: js = (
        'js/editor/kindeditor-all.js',
        'js/editor/config.js',
    )

admin.site.register(Post, PostAdmin)
# Register your models here.
admin.site.register(Comment)
admin.site.register(CV, CVAdmin)
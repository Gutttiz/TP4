from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')   # coincidencia exacta con tu modelo
    list_filter = ('fecha',)             # coincidencia exacta con tu modelo

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'nombre', 'fecha')
    list_filter = ('fecha',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )
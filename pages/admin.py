from django.contrib import admin
from .models import Page, Post
admin.site.register(Page)
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )

admin.site.register(Post,PostAdmin)
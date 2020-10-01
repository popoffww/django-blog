from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Post._meta.fields]
    list_filter = ['title']
    search_fields = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

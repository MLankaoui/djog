from django.contrib import admin
from blog.models import Posts


# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]

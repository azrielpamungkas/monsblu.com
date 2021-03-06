from pyexpat import model
from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)

from django.contrib import admin

# Register your models here.
from .models import Post

print('blog admin')

admin.site.register(Post)

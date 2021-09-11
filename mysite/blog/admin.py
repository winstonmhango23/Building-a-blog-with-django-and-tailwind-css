from django.contrib import admin
from .models import Post

#register the Post model in the admin site
admin.site.register(Post)

def __str__(self):
        return self.title
from django.contrib import admin
from .models import User, Author, Category, Post, Comment, Subscription

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subscription)

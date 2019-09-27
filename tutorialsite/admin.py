from django.contrib import admin
from tutorialsite.models import Comment, Post, Exercise, Tag
# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Exercise)
admin.site.register(Tag)

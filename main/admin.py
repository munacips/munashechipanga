from django.contrib import admin
from .models import Project, Article, Comment, Video, ProjectPic

admin.site.register([Project, Article, Comment, Video, ProjectPic])

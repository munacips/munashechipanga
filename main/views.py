from django.shortcuts import render
from .models import Project, Video, Article, Comment, ProjectPic

def home(request):
    context = {}
    return render(request,'main/home.html',context)

def projects(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request,'main/projects.html',context)

def acad(request):
    context = {}
    return render(request,'main/acad.html',context)

def contact_info(request):
    context = {}
    return render(request,'main/contact.html',context)

def blog(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request,'main/blog.html',context)

def videos(request):
    videos = Video.objects.all()
    context = {
        'videos' : videos
    }
    return render(request,'main/videos.html',context)

def project(request,id):
    project = Project.objects.get(id=id)
    pictures = ProjectPic.objects.filter(project=project)
    context = {
        'project' : project,
        'pictures' : pictures
    }
    return render(request,'main/project.html',context)

def article(request,id):
    article = Article.objects.get(id=id)
    context = {
        'article' : article
    }
    return render(request,'main/article.html',context)

def video(request,id):
    video = Video.objects.get(id=id)
    context = {
        'video' : video
    }
    return render(request,'main/video.html',context)
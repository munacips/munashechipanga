from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'main/home.html',context)

def projects(request):
    context = {}
    return render(request,'main/projects.html',context)

def acad(request):
    context = {}
    return render(request,'main/acad.html',context)

def contact_info(request):
    context = {}
    return render(request,'main/contact.html',context)

def blog(request):
    context = {}
    return render(request,'main/blog.html',context)
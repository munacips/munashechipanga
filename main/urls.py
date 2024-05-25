from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('projects/',views.projects,name="projects"),
    path('academic_info/',views.acad,name="academicInfo"),
    path('contact_info/',views.contact_info,name="contact_info"),
    path('blog/',views.blog,name="blog"),
    path('videos/',views.videos,name="videos"),
    path('project/<int:id>/',views.project,name="project"),
    path('article/<int:id>',views.article,name="article"),
    path('video/<int:id>',views.video,name="video"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
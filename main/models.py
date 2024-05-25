from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    date_started = models.DateField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='media/project_thumbnail')
    github_link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    

class ProjectPic(models.Model):
    pic = models.ImageField(upload_to='media/project_pics')
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='media/thumbnails')

    def __str__(self):
        return self.title
    

class Video(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="Video")
    views = models.IntegerField(default=0)
    video = models.FileField(upload_to='videos',max_length=500)
    thumbnail = models.ImageField(upload_to='media/thumbnails')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    video = models.ForeignKey(Video,on_delete=models.CASCADE,null=True)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=100)
        
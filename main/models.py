from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    date_started = models.DateField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='media/project_thumbnail')
    github_link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    
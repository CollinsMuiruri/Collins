from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=10)
    project_description = models.CharField(max_length=30)
    project_image = models.ImageField(upload_to = 'media/')
    project_url = models.URLField()

    def __str__(self):
        return self.project_title

    def save_project(self):
        return self.save

    def delete_project(self):
        return self.delete
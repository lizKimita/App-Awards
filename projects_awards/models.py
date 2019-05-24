from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)
    userId =models.IntegerField(default = 0)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()   

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

    def __str__(self):
        return self.bio

class Projects(models.Model):
    title = models.CharField(max_length = 30)
    project_image = models.ImageField(upload_to = 'images/')
    description = models. TextField(blank= True)
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    url = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    poster_id = models.IntegerField(default=0)


    def save_project(self):
        self.save()

    def delete_project(self):
        Projects.objects.filter().delete()
    
    @classmethod
    def get_all(cls):
        projects = Projects.objects.all()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    class Meta:
        ordering = ['-id']


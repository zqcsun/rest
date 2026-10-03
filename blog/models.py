from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200) #мале
    text = models.TextField() #велике
    active = models.BooleanField(default=True) #та або ні
    author = models.ForeignKey(User,on_delete=models.CASCADE) #список
    created = models.DateTimeField(auto_now_add=True) #встановлення дати і часу

    class Meta:
        ordering = ['id','created']
    
    def __str__(self):
        return self.title
    
class ComentsModel(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    text =  models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
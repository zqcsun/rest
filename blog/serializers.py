from rest_framework import serializers
from .models import Post,ComentsModel
from django.contrib.auth.models import User

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','email','first_name','last_name',]
class SerPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','text','created']

class SerComent(serializers.ModelSerializer):
    author_user = serializers.ReadOnlyField(source='author_username')
    class Meta:
        model = ComentsModel
        fields = ['post','title','slug','text','created','update']

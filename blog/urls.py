from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<str:post_slug>/',views.post,name='post')
]


from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
#    path('', views.home,name='linuxls-home'),
    path('', PostListView.as_view(),name='linuxls-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
#class based views look for certain naming pattern
#<app>/<model>_<viewtype>.html e.g linuxls/post_list.html
#we can change that within views.py
#URL pattern will variable within our route
    path('post/<int:pk>', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
#template will not be named as post_create.html, this one will share template with the update view
#template name is expected to be name of the model_form
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
#Since we are providing primary key in the url of the post
#we want to update then Django PostUpdateView will will take care of
#everything else even templte
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
#it expects  just a form to ask if user is sure to delte the post




    path('about/', views.about,name='linuxls-about'),
    path('fundamentals/', views.fundamentals,name='linuxls-fundamentals'),
    path('rhcsa/', views.rhcsa,name='linuxls-rhcsa'),
    ]

# blog/urls.py or blog_project/urls.py
from django.urls import path
from .views import home, create_blog, edit_blog, delete_blog, add_comment, signup,blog_list

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path('create_blog/', create_blog, name='create_blog'),
    path('edit_blog/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('add_comment/<int:blog_id>/', add_comment, name='add_comment'),
    path('signup/', signup, name='signup'),
]

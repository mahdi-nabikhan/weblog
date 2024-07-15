from django.urls import path
from django.views.generic import detail

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:post_id>/', post_detail, name='detail'),
    path('all_posts/', all_posts, name='all_posts'),
    path('category/<int:pk>',category_detail,name='category_detail'),
    path('search/', search, name='search'),
    path('add_post/', add_post, name='add_post'),

]

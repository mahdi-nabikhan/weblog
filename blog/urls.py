from django.urls import path
from django.views.generic import detail

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('all_posts/', AllPostsView.as_view(), name='all_posts'),
    path('category/<int:pk>',category_detail,name='category_detail'),
    path('search/', search, name='search'),
    path('add_post/', add_post, name='add_post'),

]

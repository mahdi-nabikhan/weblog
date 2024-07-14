from django.urls import path
from django.views.generic import detail

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:post_id>/', post_detail, name='detail'),

]

from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('list/',PostList.as_view(),name='post-list'),
   path('list/<int:pk>/',PostDetail.as_view(),name='post-detail'),
   path('auth',include('rest_framework.urls'))
]

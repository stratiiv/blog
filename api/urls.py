from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
   path('list/',PostList.as_view(),name='post-list'),
   path('list/<int:pk>/',PostDetail.as_view(),name='post-detail'),
   path('auth/',include('rest_framework.urls')),
   path('dj-rest-auth/',include('dj_rest_auth.urls')),
   path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

router=SimpleRouter()
router.register('users', UserViewSet, basename='users')
urlpatterns+=router.urls
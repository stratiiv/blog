from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics,permissions,viewsets
from .models import Post
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
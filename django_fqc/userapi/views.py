from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user

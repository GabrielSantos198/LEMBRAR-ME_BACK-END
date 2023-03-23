from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from . models import SiteContent
from . serializers import SiteContentSerializer, UserSerializer
from rest_framework.response import Response
from users.models import User

# Create your views here.
class SiteContentView(ListAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer


class CreateUserView(CreateAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        user = User.objects.create_user(username=serializer.initial_data['username'], password=serializer.initial_data['password'])
        return Response(serializer.initial_data)

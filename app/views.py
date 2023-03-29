from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from . models import SiteContent, Annotation
from . serializers import SiteContentSerializer, UserSerializer, AnnotationSerializers
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class SiteContentView(ListAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer


class AnnotationListView(ListAPIView):
    serializer_class = AnnotationSerializers
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        user = self.request.user
        queryset = Annotation.objects.filter(user=user)
        return queryset


class AnnotationDetailView(RetrieveAPIView):
    serializer_class = AnnotationSerializers
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        user = self.request.user
        queryset = Annotation.objects.filter(user=user)
        return queryset


class AnnotationCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = User.objects.get(username=self.request.user)
        request.data['user'] = user.id
        serializer = AnnotationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AnnotationUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)


    def put(self, request, pk):
        user = self.request.user
        request.data['user'] = user.id
        annotation = Annotation.objects.get(id=pk, user=user.id)
        serializer = AnnotationSerializers(annotation, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AnnotationDeleteView(DestroyAPIView):
    serializer_class = AnnotationSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Annotation.objects.filter(user=user)
        return queryset


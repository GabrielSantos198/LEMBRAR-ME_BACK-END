from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.generics import (
    ListAPIView, CreateAPIView, DestroyAPIView,
    RetrieveAPIView, UpdateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from . models import SiteContent, Annotation, Subscribe
from . serializers import SiteContentSerializer, AnnotationSerializers, SubscribeSerializers
from users.models import User

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'https://gabrielsantos198.github.io/LEMBRAR-ME_FRONT-END'


class DeleteUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        user = User.objects.filter(username=self.request.user)[0]
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


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


class AnnotationSearchView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnnotationSerializers

    def get_queryset(self):
        query = self.request.GET.get('q')
        user = self.request.user
        annotations = Annotation.objects.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(text__icontains=query),
            user=user
        )
        return annotations


class SubscribeView(CreateAPIView):
    model = Subscribe
    serializer_class = SubscribeSerializers
    permission_classes = (AllowAny,)


class ContactView(APIView):

    def post(self, request):
        if request.data['name'] and request.data['email'] and request.data['message']:
            send_mail(
                subject = f'{request.data["name"]} te envio uma mensagem pela Lembrar-me',
                message = f'E-mail: {request.data["email"]}\nMessage: {request.data["message"]}',
                from_email = request.data['email'],
                recipient_list = [settings.EMAIL_HOST_USER]
            )
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


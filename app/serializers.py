from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from . models import SiteContent, Annotation, Subscribe
from users.models import User


class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


    def create(self, validated_data):
        try:
            validate_password(validated_data['password'])
        except ValidationError:
            raise serializers.ValidationError({'password': 'weak password'})
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class AnnotationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'


class SubscribeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'



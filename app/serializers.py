from . models import SiteContent, Annotation
from rest_framework import serializers
from users.models import User

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
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


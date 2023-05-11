from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from . models import SiteContent, Annotation, Subscribe
from users.models import User


class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'


class AnnotationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'


class SubscribeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'



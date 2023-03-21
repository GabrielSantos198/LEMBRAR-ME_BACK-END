from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . models import SiteContent
from . serializers import SiteContentSerializer

# Create your views here.
class SiteContentView(ListAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer

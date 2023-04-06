from django.contrib import admin
from . models import SiteContent, Annotation, Subscribe, MessageToSubscribe

# Register your models here.
admin.site.register([SiteContent, Annotation, Subscribe, MessageToSubscribe])

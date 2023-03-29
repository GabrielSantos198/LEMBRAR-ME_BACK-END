from django.contrib import admin
from . models import SiteContent, Annotation

# Register your models here.
admin.site.register([SiteContent, Annotation])

from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

# Create your models here.
class SiteContent(models.Model):
    about_platform = models.TextField()
    values_card_0 = models.TextField()
    values_card_1 = models.TextField()
    values_card_2 = models.TextField()
    about_developer = models.TextField()
    developer_img = models.ImageField(upload_to='developer/')
    privacy_policies = models.TextField()

    def __str__(self):
        return 'Site Content'


class Annotation(TimeStampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    summary = models.CharField(max_length=150, blank=False)
    text = models.TextField()

    class Meta:
        ordering = ('-modified',)

    def __str__(self):
        return self.title


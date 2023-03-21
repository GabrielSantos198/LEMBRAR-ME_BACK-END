from django.db import models

# Create your models here.
class SiteContent(models.Model):
    about_platform = models.TextField()
    values_card_0 = models.TextField()
    values_card_1 = models.TextField()
    values_card_2 = models.TextField()
    about_developer = models.TextField()
    developer_img = models.ImageField(upload_to='developer/')

    def __str__(self):
        return 'Site Content'

# Generated by Django 4.1.7 on 2023-03-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_platform', models.TextField()),
                ('values_card_0', models.TextField()),
                ('values_card_1', models.TextField()),
                ('values_card_2', models.TextField()),
                ('about_developer', models.TextField()),
                ('developer_img', models.ImageField(upload_to='developer/')),
            ],
        ),
    ]

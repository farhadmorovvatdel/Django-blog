# Generated by Django 4.1.3 on 2023-01-20 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0020_alter_blog_likes_alter_blog_unlikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='userlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='unlikes',
            field=models.ManyToManyField(related_name='userunlike', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1 on 2022-08-17 14:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("intro", "0004_partnerall_like_partnerall_like_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="like_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="partnerbusiness",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="likes_business", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="partnerbusiness",
            name="like_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="partnerhumanity",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="likes_humanity", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="partnerhumanity",
            name="like_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="partnerall",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="likes_all", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
# Generated by Django 4.1 on 2022-08-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("intro", "0008_alter_partner_like_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="like_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

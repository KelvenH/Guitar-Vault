# Generated by Django 3.2.9 on 2021-11-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0008_auto_20211117_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
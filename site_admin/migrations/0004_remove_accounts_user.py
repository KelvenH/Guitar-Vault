# Generated by Django 3.2.9 on 2022-01-26 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0003_auto_20220126_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='user',
        ),
    ]
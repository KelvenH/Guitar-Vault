# Generated by Django 3.2.9 on 2021-11-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0011_auto_20211129_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='controls',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0012_alter_guitar_controls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='controls',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

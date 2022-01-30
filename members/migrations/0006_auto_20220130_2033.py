# Generated by Django 3.2.9 on 2022-01-30 20:33

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_delete_membersplans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='default_country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='default_county',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='default_phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='default_postcode',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='default_street_address1',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='default_town_or_city',
            field=models.CharField(max_length=40),
        ),
    ]

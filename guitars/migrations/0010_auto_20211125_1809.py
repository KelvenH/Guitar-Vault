# Generated by Django 3.2.9 on 2021-11-25 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0009_guitar_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guitars.category'),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='frets',
            field=models.DecimalField(choices=[(20, 20), (22, 22), (24, 24)], decimal_places=0, default=22, max_digits=2),
        ),
    ]

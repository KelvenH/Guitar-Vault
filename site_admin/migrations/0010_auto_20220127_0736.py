# Generated by Django 3.2.9 on 2022-01-27 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0009_alter_accounts_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='plec_brnz',
            new_name='plectrum_balance',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='plec_gold',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='plec_plat',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='plec_slvr',
        ),
    ]

# Generated by Django 3.2.6 on 2022-08-16 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birth',
            new_name='birthday',
        ),
    ]

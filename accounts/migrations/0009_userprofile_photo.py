# Generated by Django 3.2.6 on 2022-08-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_userprofile_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Аватарка'),
        ),
    ]

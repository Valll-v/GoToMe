# Generated by Django 3.2.6 on 2022-08-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220816_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(default='12-10-1975'),
        ),
    ]

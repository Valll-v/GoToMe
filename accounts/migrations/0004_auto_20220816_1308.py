# Generated by Django 3.2.6 on 2022-08-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='Amsterdam', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='NetherLand', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default='Administration of this city', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='admin', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Joseph Admin', max_length=50),
        ),
    ]

# Generated by Django 3.0 on 2020-10-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]

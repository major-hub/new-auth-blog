# Generated by Django 3.1.5 on 2021-01-13 04:43

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='userProfile/'),
        ),
    ]

# Generated by Django 3.2.15 on 2022-10-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0002_comment_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]

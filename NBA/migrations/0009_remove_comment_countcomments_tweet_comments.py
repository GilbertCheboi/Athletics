# Generated by Django 4.1.3 on 2022-12-10 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0008_alter_tweet_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='countcomments',
        ),
        migrations.AddField(
            model_name='tweet',
            name='comments',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, related_name='Baseballcomments', to='NBA.comment'),
            preserve_default='True',
        ),
    ]
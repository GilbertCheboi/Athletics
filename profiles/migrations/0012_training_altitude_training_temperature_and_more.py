# Generated by Django 4.1.6 on 2023-02-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_academics_training_delete_championleague_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='Altitude',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='Temperature',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='acitvity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='mentalstate',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.2 on 2021-06-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgallery',
            name='mainImage',
            field=models.BooleanField(default=True),
        ),
    ]

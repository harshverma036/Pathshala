# Generated by Django 3.2.2 on 2021-07-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutAndStaffs', '0004_auto_20210707_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

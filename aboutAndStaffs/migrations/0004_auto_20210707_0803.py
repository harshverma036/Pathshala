# Generated by Django 3.0.5 on 2021-07-07 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutAndStaffs', '0003_merge_20210707_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

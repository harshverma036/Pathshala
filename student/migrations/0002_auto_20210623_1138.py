# Generated by Django 3.0.5 on 2021-06-23 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.Teachers'),
        ),
    ]

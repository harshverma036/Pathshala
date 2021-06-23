# Generated by Django 3.0.5 on 2021-06-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=10)),
                ('strength', models.IntegerField(default=0)),
                ('class_teacher', models.CharField(max_length=15)),
                ('tution_fees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(default=0)),
                ('full_name', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=1)),
                ('session_start', models.DateField()),
                ('session_end', models.DateField()),
                ('dob', models.DateField()),
                ('father_name', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('attendence', models.IntegerField(default=0)),
                ('createdBy', models.CharField(max_length=20)),
                ('createdAt', models.DateTimeField()),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.Students_Class')),
            ],
        ),
        migrations.CreateModel(
            name='Class_Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.Students_Class')),
            ],
        ),
    ]

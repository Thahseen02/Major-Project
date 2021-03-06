# Generated by Django 2.0.5 on 2019-04-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, verbose_name='Name')),
                ('roll_number', models.CharField(max_length=25, verbose_name='Roll Number')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'other')], max_length=1, verbose_name='Gender')),
                ('cgpa', models.FloatField(verbose_name='CGPA')),
                ('school_grade', models.FloatField(verbose_name='12th Grade')),
                ('internship', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Internship Experience')),
                ('os', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('R', 'R')], max_length=1, verbose_name='Grade in Operating Sytems')),
                ('networks', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('R', 'R')], max_length=1, verbose_name='Grade in Networks')),
                ('dbms', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('R', 'R')], max_length=1, verbose_name='Grade in DBMS ')),
                ('dsa', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('R', 'R')], max_length=1, verbose_name='Grade in DSA')),
                ('interviews', models.FloatField(verbose_name='Number Of Interviews Attended')),
            ],
        ),
    ]

# Generated by Django 2.0.5 on 2019-04-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=10000)),
                ('category', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], max_length=1)),
                ('subject', models.CharField(choices=[('OS', 'OS'), ('DBMS', 'DBMS'), ('DSA', 'DSA'), ('NT', 'NETWORKS')], max_length=7)),
                ('a_choice', models.CharField(max_length=10000)),
                ('b_choice', models.CharField(max_length=10000)),
                ('c_choice', models.CharField(max_length=10000)),
                ('d_choice', models.CharField(max_length=10000)),
                ('correct', models.CharField(max_length=10000)),
            ],
        ),
    ]

# Generated by Django 2.2.11 on 2020-03-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='0000000', max_length=30),
        ),
    ]

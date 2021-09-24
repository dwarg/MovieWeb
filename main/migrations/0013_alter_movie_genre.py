# Generated by Django 3.2.3 on 2021-05-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Fantasy', 'Fantasy'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Adventure', 'Adventure'), ('Sci-Fi', 'Sci-Fi'), ('Thriller ', 'Thriller'), ('Western', 'Western'), ('War', 'War'), ('Crime', 'Crime')], max_length=35),
        ),
    ]
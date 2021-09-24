# Generated by Django 3.2.2 on 2021-05-09 20:36

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Akcja', 'Akcja'), ('Fantasy', 'Fantasy'), ('Komedia', 'Komedia'), ('Dramat', 'Dramat'), ('Horror', 'Horror'), ('Komedia', 'Komedia'), ('Przygodowy', 'Przygodowy'), ('Sci-Fi', 'Sci-Fi'), ('Thriller ', 'Thriller'), ('Western', 'Western'), ('Wojennny', 'Wojennny')], default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='typ',
            field=models.CharField(choices=[('Film', 'Film'), ('Serial', 'Serial')], default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
# Generated by Django 3.2.3 on 2021-05-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='seasons',
            field=models.CharField(default='how much seasons?', max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.URLField(default='Example: https://www.youtube.com/embed/dQw4w9WgXcQ'),
        ),
    ]
# Generated by Django 3.0.14 on 2021-05-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_review_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date',
        ),
    ]
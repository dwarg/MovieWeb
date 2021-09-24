from django.db import models
from django import forms
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Movie(models.Model):

    GENRES = (
       ('Action', ('Action')),
       ('Adventure', ('Adventure')),
       ('Animation', ('Animation')),
       ('Comedy', ('Comedy')),
       ('Crime', ('Crime')),
       ('Drama', ('Drama')),
       ('Documentary', ('Documentary')),
       ('Fantasy', ('Fantasy')),
       ('Horror', ('Horror')),
       ('Romance', ('Romance')),
       ('Sci-Fi', ('Sci-Fi')),
       ('Thriller ', ('Thriller')),
       ('Western', ('Western')),
       ('War', ('War')),

    )

    TYPES = (
       ('Movie', ('Movie')),
       ('TV Series', ('TV Series')),
    )

    typ = models.CharField(max_length=35,
       choices=TYPES,
    )
    
    seasons = models.IntegerField(null=True, blank=True)

    genre = models.CharField(max_length=35,
       choices=GENRES,
    )

    title = models.CharField(max_length=300)
    creators = models.CharField(max_length=300)
    cast = models.CharField(max_length=800)
    description = models.TextField(max_length=5000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.URLField(default='Example: https://i.imgur.com/ID.jpg', null=False)
    video = models.URLField(default='Example: https://www.youtube.com/embed/dQw4w9WgXcQ', null=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 250)

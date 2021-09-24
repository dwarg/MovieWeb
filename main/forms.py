from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'creators', 'cast', 'description', 'genre', 'typ', 'seasons', 'release_date', 'image', 'video')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")
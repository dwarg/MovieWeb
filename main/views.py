from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import *
from .forms import *
from django.db.models import Avg

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:list")
      
	form = ContactForm()
	return render(request, "main/contact.html", {'form':form})

def list(request):
    query = request.GET.get("title")
    allMovies = None
    if query:
        allMovies = Movie.objects.filter(name__icontains=query)
    else:
        allMovies = Movie.objects.all()

    context = {
        "movies": allMovies,
    }

    return render(request, 'main/index.html', context)

def detail(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=id).order_by("-rating")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "movie": movie,
        "reviews": reviews,
        "average": average
    }
    return render(request, 'main/details.html', context)

def add_movies(request):
    if request.user.is_staff:
        if request.user.is_authenticated:
            if request.method == "POST":
                form = MovieForm(request.POST or None)

            # check if the form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:list")
            else:
                form = MovieForm()
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add"})
    return redirect("accounts:login")


def edit_movies(request, id):
    if request.user.is_staff:
        if request.user.is_authenticated:
            movie = Movie.objects.get(id=id)

            if request.method == "POST":
                form = MovieForm(request.POST or None, instance=movie)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = MovieForm(instance=movie)
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Edit"})
    return redirect("main:detail", id)


def delete_movies(request, id):
    if request.user.is_staff:
        if request.user.is_authenticated:
            movie = Movie.objects.get(id=id)
            movie.delete()
            return redirect("main:list")
    return redirect("main:detail", id)


def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form": form})
    else:
        return redirect("accounts:login")


# edit the review
def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Out or range. Please select rating from 0 to 10."
                        return render(request, 'main/editreview.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("main:detail", movie_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', {"form": form})
        else:
            return redirect("main:detail", movie_id)
    else:
        return redirect("accounts:login")


def delete_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            review.delete()

        return redirect("main:detail", movie_id)

    else:
        return redirect("accounts:login")

from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Book, UserRating

def home_page(request):
    return render(request, 'Hub/templates/Hub/base.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Hub/templates/Hub/book_list.html', {'books': books})

#@login_required
def book_detail(request, book_id):
    book = None
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        book = get_object_or_404(Book, pk=book_id)
        try:
            user_rating = UserRating.objects.get(book=book, user=request.user)
        except UserRating.DoesNotExist:
            user_rating = None

        if request.method == 'POST':
            score = int(request.POST['score'])
            if user_rating:
                user_rating.score = score
                user_rating.save()
            else:
                user_rating = UserRating.objects.create(
                    book=book,
                    user=request.user,
                    score=score
                )
            # redirect to the same page to avoid resubmitting the form
            return HttpResponseRedirect(reverse('book_detail', args=(book_id,)))

        # get all ratings for the book
        ratings = UserRating.objects.filter(book=book)[:5]

        context = {
            'book': book,
            'user_rating': user_rating,
            'ratings': ratings
        }
        return render(request, 'Hub/templates/Hub/book_detail.html', context)
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/accounts/login/')

def new_rating(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'Hub/templates/Hub/rate_book.html', {'book': book})

def top_books(request):
    top_books = Book.objects.annotate(avg_rating=Avg('userrating__score')).order_by('-avg_rating')[:10]
    context = {'top_books': top_books}
    return render(request, 'Hub/templates/Hub/top_books.html', context)

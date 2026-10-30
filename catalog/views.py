from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Book, Author, BookInstance, Genre, Language

def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #the 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Generate coutn of genres containing 'fiction'
    num_genres_fiction = Book.objects.filter(genre__name__icontains='fiction').count()

    # Generate count of titles containing 'the'
    num_titles_the = Book.objects.filter(title__icontains='the').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_fiction': num_genres_fiction,
        'num_titles_the':num_titles_the
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book_detail'
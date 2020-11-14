from django.shortcuts import render, redirect
from fullybooked.models import Book
from fullybooked.forms import NewBookForm, ReviewBookForm


# Create your views here.

# responsible for the main page
def index(request):
    # querey the database for a list of all books stored.
    # Ordered by author alphabetically?
    book_list = Book.objects.order_by('author')

    # place the book_list in the context_dict dictionary to be passed to the template engine
    context_dict = {'books': book_list}

    return render(request, 'fullybooked/index.html', context=context_dict)


# creating a view for use with the New Book Form to add a book to your shelf
def add_book(request):
    form = NewBookForm()

    if request.method == 'POST':
        form = NewBookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/fullybooked/')
        else:
            # if the form has errors
            print(form.errors)

    return render(request, 'fullybooked/add_book.html', {'form': form})


# creating a view for use with the Review Book Form, to rate a book
def review_book(request):
    form = ReviewBookForm()

    if request.method == 'POST':
        form = ReviewBookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/fullybooked/')
        else:
            # if the form has errors
            print(form.errors)

    return render(request, 'fullybooked/review_book.html', {'form': form})

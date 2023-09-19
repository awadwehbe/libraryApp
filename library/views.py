
from django.shortcuts import render #render used to render HTML templates and return HTTP responses
from .models import Book #Book is the model that represents books in your application.
from .forms import BookSearchForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

from django.db.models import Q

def book_list(request):
    books = Book.objects.all()
    search_query = request.GET.get('search_query', '')

    if search_query:
        # Use Q objects to perform a case-insensitive search across title, author, and publication year
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(publication_year__icontains=search_query)|
            Q(category__icontains=search_query)
        )

    return render(request, 'library/book_list.html', {'books': books, 'search_query': search_query})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/delete_book_confirm.html', {'book': book})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'library/edit_book.html', {'form': form, 'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'library/add_book.html', {'form': form})
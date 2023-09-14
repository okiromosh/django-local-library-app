from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.decorators import login_required
import datetime
from .forms import *
from django.urls import reverse

# Create your views here.


def index(request):
    num_authors = Author.objects.all().count()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context)


def booksView(request):
    books_list = Book.objects.all()

    books_per_page = 2
    paginator = Paginator(books_list, books_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books_list': books_list,
        'page_obj': page_obj,
    }
    return render(request, 'catalog/book_list.html', context)


def bookDetail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404('Book does not Exist!')

    context = {
        'book': book
    }

    return render(request, 'catalog/book_detail.html', context)


def authorsView(request):
    author_list = Author.objects.all()

    authors_per_page = 2
    paginator = Paginator(author_list, authors_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'catalog/author_list.html', context)


def authorDetail(request, pk):
    try:
        author = Author.objects.get(id=pk)
    except Author.DoesNotExist:
        raise Http404('Author does not Exist')

    books_written = Book.objects.filter(author=author)

    context = {
        'author': author,
        'books_written': books_written,
    }

    return render(request, 'catalog/author_detail.html', context)


@login_required()
def loaned_books_by_user(request):
    book_instances = (
        BookInstance.objects.filter(borrower=request.user).filter(status__exact='o').order_by('due_back')
    )

    paginator = Paginator(book_instances, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'book_instances': page_obj
    }
    return render(request, 'catalog/bookinstance_list_borrowed_user.html', context )


@login_required()
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_data']
            book_instance.save()

            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date })

    context = {
        'form': form,
        'book_instance': book_instance
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


@login_required()
def create_author(request,):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author', pk=author.id)
    else:
        form = AuthorForm()  # Initialize an empty form

    return render(request, 'catalog/author_form.html', {'form': form})


@login_required()
def update_author(request, pk):
    author = get_object_or_404(Author, id=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author.save()
            return redirect('author', id=pk)
    else:
        form = AuthorForm(instance=author)

    context = {
        'form': form
    }
    return render(request, 'catalog/author_form.html', context)


@login_required()
def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        author.delete()  # Delete the author from the database
        return redirect('authors')  # Redirect to a list view of authors

    context = {
        'author': author
    }

    return render(request, 'catalog/confirm_author_delete.html')


@login_required()
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book', pk=book.id)
    else:
        form = BookForm()  # Initialize an empty form

    return render(request, 'catalog/book_form.html', {'form': form})


@login_required()
def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form
    }
    return render(request, 'catalog/book_form.html', context)


@login_required()
def delete_book(request, pk):
    book = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        book.delete()  # Delete the author from the database
        return redirect('books')  # Redirect to a list view of authors

    context = {
        'book': book
    }

    return render(request, 'catalog/confirm_author_delete.html')






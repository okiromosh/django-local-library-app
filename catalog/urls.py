from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.booksView, name='books'),
    path('book/<int:pk>', views.bookDetail, name='book'),
    path('book/create/', views.create_book, name='create-book'),
    path('book/<int:pk>/update/', views.update_book, name='update-book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete-book'),

    path('authors', views.authorsView, name='authors'),
    path('author/<int:pk>', views.authorDetail, name='author'),
    path('author/create/', views.create_author, name='create-author'),
    path('author/<int:pk>/update/', views.update_author, name='update-author'),
    path('author/<int:pk>/delete/', views.delete_author, name='delete-author'),

    path('mybooks/', views.loaned_books_by_user, name='my-borrowed'),

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

]

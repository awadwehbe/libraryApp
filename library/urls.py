from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
     path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
     path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
     path('book/add/', views.add_book, name='add_book'),
]


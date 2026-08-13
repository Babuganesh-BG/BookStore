from django.shortcuts import render, redirect
from .models import Book

def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )

    books = Book.objects.all()
    return render(request, 'Books/home.html', {'books': books})


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.save()

    return render(request, 'Books/edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()

    return redirect('home')
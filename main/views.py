from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import BookStore

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def books(request):
    bookstore_list = BookStore.objects.all()
    return render(request, "books.html", {"bookstore_list": bookstore_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = BookStore(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year  )
    book.save()
    return redirect(books)

def delete_book(request, id):
    book = BookStore.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_book(request, id):
    book = BookStore.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(books)

def unmark_book(request, id):
    book = BookStore.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(books)
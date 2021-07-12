from django.shortcuts import render
from .models import book_detail
from django.views.generic import ListView, DetailView


def createbook(request):
    if request.method == 'POST':
        if request.POST.get('Book_name') and request.POST.get('Author') and request.POST.get(
                'genre') and request.POST.get('language'):
            post = book_detail()
            post.Book_name = request.POST.get('Book_name')
            post.Author = request.POST.get('Author')
            post.genre = request.POST.get('genre')
            post.language = request.POST.get('language')
            post.save()
            books = book_detail.objects.all()

            return render(request, 'Book/book_forms.html', {'Book': books})

    else:
        return render(request, 'Book/book_form.html')


def Bookinfo(request):
    if request.method == 'POST':
        if request.POST.get('genre'):
            books = book_detail.objects.filter(genre=request.POST.get('genre'))
            return render(request, 'Book/book_forms.html', {'Book': books})
        elif request.POST.get('language'):
            books = book_detail.objects.filter(language=request.POST.get('language'))
            return render(request, 'Book/book_forms.html', {'Book': books})
        elif request.POST.get('genre') and request.POST.get('language'):
            books = book_detail.objects.filter(genre=request.POST.get('genre'), language=request.POST.get('language'))
            return render(request, 'Book/book_forms.html', {'Book': books})
    else:
        books = book_detail.objects.all()
        print('myoutput', books)
        return render(request, 'Book/book_forms.html', {'Book': books})

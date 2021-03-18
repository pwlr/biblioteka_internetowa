from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Book
from .forms import BookCreate, AuthForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main(request):
    allPublishedBooks = Book.objects.all().filter(delete=False)
    loginForm = AuthForm()
    if request.user.is_authenticated:
        return render(request, 'biblioteka/main.html', {'allPublishedBooks': allPublishedBooks})
    return render(request, 'biblioteka/login.html', {'allPublishedBooks': allPublishedBooks, 'loginForm': loginForm})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def userPanel(request):
    if request.user.is_authenticated:
        userName = request.user.get_username()
        allUserBooks = Book.objects.filter(stworzono_przez=request.user, delete=False)

        context = {
            'userName': userName,
            'allPublishedBooks': allUserBooks,
        }
        return render(request, 'biblioteka/read.html', context)
    else:
        return redirect('/')


def userAuth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/panel/')
    else:
        return redirect('/')


@login_required
def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newBook = BookCreate(request.POST, request.FILES)
            if newBook.is_valid():
                bookFiles = newBook.save(commit=False)
                bookFiles.stworzono_przez = request.user.username
                bookFiles.save()
                newBook.save()
                return redirect('/panel/')
            else:
                return redirect('/panel/')
    else:
        print('użytkownik niezalogowany')
        return redirect('/')


@login_required
def create(request):
    if request.user.is_authenticated:
        newBookForm = BookCreate()
        userName = request.user.get_username()
        return render(request, 'biblioteka/create.html', {'newBookForm': newBookForm, 'userName': userName})
    else:
        print('użytkownik niezalogowany')
        return redirect('/')


@login_required
def update(request, pk):
    if request.user.is_authenticated:
        current_book = Book.objects.get(pk=pk)
        BookForm = BookCreate(instance=current_book)
        userName = request.user.get_username()
        return render(request, 'biblioteka/update.html',
                      {'BookForm': BookForm, 'current_book': current_book, 'userName': userName})
    else:
        return redirect('/')


@login_required
def update_database(request, pk):
    current_book = Book.objects.get(pk=pk)
    book = BookCreate(instance=current_book)
    book = BookCreate(request.POST, instance=current_book)
    book.save()
    return redirect('/panel/')


@login_required
def delete(request, pk):
    if request.user.is_authenticated:
        current_book = Book.objects.get(pk=pk)
        current_book.delete = True
        current_book.save()
        return redirect('/panel/')
    else:
        return redirect('/')
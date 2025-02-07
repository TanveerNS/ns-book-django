from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

# @login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def add_book(request):
    if request.method == 'POST':
        # If the form is submitted with POST request
        form = BookForm(request.POST, request.FILES)  # Handle file upload as well (for cover_image)
        if form.is_valid():
            form.save()  # Save the new book in the database
            return redirect('home')  # Redirect after the book is added (you can change this to redirect to any page you want)
    else:
        form = BookForm()  # Empty form for GET request

    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    # Get all books from the database
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})
def user_view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list') 

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')  # Redirect to the book list after successful edit
        else:
            messages.error(request, 'There was an error in the form submission.')

    else:
        form = BookForm(instance=book)  # Prefill form with book data

    return render(request, 'edit_book.html', {'form': form, 'book': book})
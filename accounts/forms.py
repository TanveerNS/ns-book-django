from django import forms
from django.contrib.auth.models import User
from .models import Book

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'genre', 'publisher', 'publication_date', 'language', 'cover_image', 'description', 'price', 'format']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
from django import forms
from .models import Book


class AuthForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'data_publikacji': forms.DateInput(format='%m%d%y',
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
            'delete': forms.HiddenInput(),
            'stworzono_przez': forms.HiddenInput()
        }

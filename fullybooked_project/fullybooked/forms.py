from django import forms
from fullybooked.models import Book


class NewBookForm(forms.ModelForm):
    title = forms.CharField(max_length=150, help_text="Please enter the book title.")
    author = forms.CharField(max_length=80, help_text="Please enter the author name.")
    rating = forms.IntegerField(initial=0)

    class Meta:
        model = Book
        fields = ('title', 'author')


class ReviewBookForm(forms.ModelForm):
    rating = forms.IntegerField(initial=0)

    class Meta:
        model = Book
        fields = ('rating',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

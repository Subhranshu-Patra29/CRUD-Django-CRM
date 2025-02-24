from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from .models import Record

# Register a user
class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

# Create a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country', 'zipcode']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john.doe@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(123) 456-7890'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Main St'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anytown'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CA'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USA'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345'}),
        }

# Update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country', 'zipcode']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john.doe@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(123) 456-7890'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Main St'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anytown'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CA'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USA'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345'}),
        }
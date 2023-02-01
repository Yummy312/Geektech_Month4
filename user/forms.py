from django import forms


class AuthForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(widget=forms.PasswordInput, min_length=3)


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3)
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=3)
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=3)
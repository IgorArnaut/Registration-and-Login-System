from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=50)
    phone_number = forms.CharField(required=True, max_length=20)
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput)
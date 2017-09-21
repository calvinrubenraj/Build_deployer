from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(lable='username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(lable='password', widget=forms. PasswordInput(attrs={'placeholder': 'Password'}))
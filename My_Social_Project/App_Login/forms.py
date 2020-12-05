from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':"email"}))
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':"username"}))
    password1 = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':"Password"}))
    password2 = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':"Password Confirmation"}))
    class Meta:
        model = User
        fields = ('email','username','password1','password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':"Username"}))
    password = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':"Password"}))


class EditProfile(forms.ModelForm):
    date_of_birth = forms.DateField(label="Date of Birth",widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude = ('user',) 
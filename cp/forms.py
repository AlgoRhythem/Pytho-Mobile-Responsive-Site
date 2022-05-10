#Import what you need:
from django import forms

#Create our 'form' class:
class signupForm(forms.Form):
    #create the form:
    fname = forms.CharField(max_length=50, label='First name', widget=forms.TextInput(attrs={'placeholder': 'enter first name', 'style': 'height: 25px; border-radius: 5px; background-color: aliceblue;'})) #This is our first input field
    lname = forms.CharField(max_length=50, label='Last name', widget=forms.TextInput(attrs={'placeholder': 'enter last name', 'style': 'height: 25px; border-radius: 5px; background-color: aliceblue;'}))
    email = forms.CharField(max_length=100, label='Your email', widget=forms.EmailInput(attrs={'placeholder': 'enter email address', 'style': 'height: 25px; border-radius: 5px; background-color: aliceblue;'})) #Validate email style (@ symbol)
    password = forms.CharField(max_length=100, label='New password', widget=forms.PasswordInput(attrs={'placeholder': 'enter a password', 'style': 'height: 25px; border-radius: 5px; background-color: aliceblue;'})) #Validate password style (*** symbol)

class loginForm(forms.Form):
    email = forms.CharField(max_length=100, label='enter your email', widget=forms.EmailInput(attrs={'placeholder': 'enter email address', 'style': 'height: 25px; border-radius: 5px; background-color: aliceblue;'}))
    password = forms.CharField(max_length=100, label='enter your password', widget=forms.PasswordInput(attrs={'placeholder': 'enter a password', 'style': 'height: 25px; border-radius: 5px; background-color: aliceblue;'}))
    
from unicodedata import name
from django.shortcuts import redirect, render
#Import the forms:
from .forms import loginForm, signupForm, contactForm
#Import the models:
from .models import user
from .models import contact
#Import serializer:
from django.core import serializers
#Import JSON:
import json

#Import server:
'''from django.http import HttpResponse''' #Don't need this right now

# Create your views here (by creating a function that will display the page).
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contactPage(request):
    if request.method == 'POST':
        #create variable for the form:
        contact_form = contactForm(request.POST)
        if contact_form.is_valid():
            #create variables to store user input:
            userName = contact_form.cleaned_data['name']
            userEmail = contact_form.cleaned_data['email']
            userSubject = contact_form.cleaned_data['subject']
            userMessage = contact_form.cleaned_data['message']
            #insert the data into our 'contact' database from our model:
            contact_data = contact(dbname = userName, dbemail = userEmail, dbsubject = userSubject, dbmessage = userMessage)
            contact_data.save()
            success_message = 'Your message has been sent!'
            contactF = contactForm()
            return render(request, 'pages/contact.html', {'contactForm': contactF, 'successMessage': success_message})
    else:
        contactF = contactForm()
        return render(request, 'pages/contact.html', {'contactForm': contactF})

def services(request):
    return render(request, 'pages/services.html')

def profile(request):
    if request.session.has_key('firstName'): #better to use the session variable for the email (userEmail)
        return render(request, 'pages/profile.html', {'ssnLastName': request.session['lastName'], 'email': request.session['userEmail'], 'name': request.session['firstName']}) #Session variable: regular
    else:
        request.session['error'] = "You need to log in first to go to the profile"
        return redirect('/login')

def signup(request):
    #Check how user arrived to the page:
    if request.method == 'POST':
        #take/store user data: 
        submitted_form = signupForm(request.POST)
        if submitted_form.is_valid(): #store the data in session and regular variables below
            request.session['firstName'] = submitted_form.cleaned_data['fname']
            request.session['lastName'] = submitted_form.cleaned_data['lname']
            request.session['userEmail'] = submitted_form.cleaned_data['email']
            userPass = submitted_form.cleaned_data['password']
            #if user exists:
            if user.objects.filter(dbemail = request.session['userEmail']):
                errorMessage = "This user already exists!"
                formS = signupForm()
                return render(request, 'pages/signup.html', {'errorM': errorMessage, 'signupForm': formS})
            else:
                #insert the data into our 'user' database from our model:
                user_data = user(dbfname = request.session['firstName'], dblname =  request.session['lastName'], 
                dbemail = request.session['userEmail'], dbpassword = userPass)
                user_data.save()
            
                #if successful, redirect to profile page:
                '''return render(request, 'pages/signup.html', {'Name': firstName})'''#used to test
                return redirect('/profile')
    else:
        #Create a variable for our form:
        form = signupForm()
        return render(request, 'pages/signup.html', {'signupForm': form})

def login(request):
    #check if the user came through the 'post' method:
    if request.method == 'POST':
        #take/store user data: 
        submitted_form = loginForm(request.POST)
        if submitted_form.is_valid(): #store the data in session and regular variables below
            #create variables for user's email and password to be stored:
            userEmail = submitted_form.cleaned_data['email']
            userPass = submitted_form.cleaned_data['password']
           
            #log in process: verify if user email exists in the database:
            member = user.objects.filter(dbemail = userEmail, dbpassword = userPass)
            if member:#if user exists:
                member = serializers.serialize('json', member)
                request.session['user'] = member #store the user email and password in session the variable
                #unpack your member data (first name and last name) and store each peice of data in one session variable:
                userinfo = json.loads(member)
                request.session['firstName'] = userinfo[0]['fields']['dbfname']
                request.session['lastName'] = userinfo[0]['fields']['dblname']
                request.session['userEmail'] = userinfo[0]['fields']['dbemail']
                return redirect('/profile')
           
            else: #else, if they don't:
                loginError = "Incorrect email or password"
                #create variable for login form:
                formL = loginForm()
                return render(request, 'pages/login.html', {'errorL': loginError, 'userLogin': formL})
    else:
        #check for session varialbes, if none, throw error:
        if request.session.has_key('error'):
            error = request.session['error']
        else:
            error = ""
        #create variable for login form:
        formL = loginForm()
        #render the login page:
        return render(request, 'pages/login.html', {'error': error, 'userLogin': formL})
    
def logout(request):
    #Delete session variables and redirect to login page:
    del request.session['firstName']
    del request.session['lastName']
    del request.session['userEmail']
    if request.session.has_key('error'):
        del request.session['error']
    return redirect('/login')
from django.shortcuts import render, redirect
from .forms import registerform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# view to register user 
# if user fill the form with appropriate data format, form will be valid and user will move to next page i.e login page
# else user will redirect to the register page again
def register(response):
	if response.method=="POST":
		form=registerform(response.POST)
		if form.is_valid():
			form.save()
		return redirect ('/login')
	else:
		form=registerform()
	return render(response, "register/register.html", {"form":form})
	
# view is written to check login condition
# if user is successfully registered and filled the correct login info i.e. username ans password, user will be taken to index page
# on index page user can perform CRUD (Create, Read, Update, Delete) operations on employee list
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/employees')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})

# on Log out, user will be redirected to the login page
def logout_request(request):
    logout(request)
    return redirect("/login")
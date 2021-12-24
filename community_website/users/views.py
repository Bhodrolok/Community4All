from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterUserForm
from services.models import User

# Create your views here.

def login_user(request):
	## view for rendering login page
	if request.method == "POST":
		# get the post parameters
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		
		# Check for valid login
		if user is not None:
			login(request, user)
			messages.success(request, ": Logged in successfully.")
			return redirect('home')
		else:
			# Return an 'invalid login' error message.
			messages.success(request, ("Credentials not found in database. Try again."))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("Logged out."))
	return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			# Save this in the Service/User Table
			u = User(
				first_name = form.cleaned_data['first_name'],
				last_name = form.cleaned_data['last_name'],
				email = form.cleaned_data['email'],
				address = form.cleaned_data['address'],
				postal_code = form.cleaned_data['postal_code'],
				phone = form.cleaned_data['phone'])
			u.save()
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate(username=username, password=password)
			login(request, user)

			messages.success(request, ("Account creation successfull."))
			return redirect('home')
	else:
		form = RegisterUserForm()

	return render(request, 'authenticate/register_user.html', {'form':form})

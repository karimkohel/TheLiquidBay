from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created successfully for : {username}')
			login(request, user)
			return redirect('main:home')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{form.error_messages[msg]}")
			
	else:
		form = UserRegisterForm()
	context = {
	'title':'Register',
	'form':form
	}
	return render(request,'user/register.html',context)


@login_required
def profile(request):
	context = {
	'title':'Profile'
	}

	return render(request, 'user/profile.html',context)

@login_required
def profile_edit(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f"Successfully updated Profile")
			return redirect('user:profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
	'u_form': u_form ,
	'p_form': p_form
	}

	return render(request, 'user/profile_edit.html',context)


# def password_reset_done(request):
# 	return render(request, 'user/password_reset_done.html')
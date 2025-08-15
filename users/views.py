from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST or None, instance=request.user)
        prof_upd_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance= request.user.profilemodel)
        if update_form.is_valid() and prof_upd_form.is_valid():
            update_form.save()
            prof_upd_form.save()
            return redirect('user_profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        prof_upd_form = ProfileUpdateForm(instance= request.user.profilemodel)
    context = {
        "update_form": update_form,
        "prof_upd_form": prof_upd_form,
    }
    return render(request, 'users/profile.html', context)
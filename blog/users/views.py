from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CounseleeUpdateForm, CounseleeRegisterForm, CounseleePictureForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    form = CounseleeRegisterForm()
    if request.method == 'POST':
        form = CounseleeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # print(username)
            messages.success(request, f'Account created for {username}. You can now Login')
            return redirect('login')
        else:
            form = CounseleeRegisterForm(request.POST)
            messages.error(request, 'Failed to Create Account')

    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = CounseleeUpdateForm(request.POST, instance=request.user)
        p_form = CounseleePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
        u_form = CounseleeUpdateForm(instance=request.user)
        p_form = CounseleePictureForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)




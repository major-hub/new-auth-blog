from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserUpdateForm ,ProfileImage


def register(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно был создан')
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': "Registration",
    }
    return render(request, 'users/registration.html', context)


@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if img_profile.is_valid() and update_user.is_valid():
            img_profile.save()
            update_user.save()
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }
    return render(request, 'users/profile.html', data)

from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
from registration.forms import User

from typer_app.forms import UserForm, ProfileForm
from typer_app.models import UserProfile


@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            # if user_form.changed_data:
            #     user = User.objects.get(pk=request.user.pk)
            #     for data in user_form.changed_data:
            #         user.data = user_form.cleaned_data.get(data)
            #     user.save
            # if profile_form.changed_data:
            #     user_profile = UserProfile.objects.get(pk=request.user.userprofile.pk)
            #     for data in profile_form.changed_data:
            #         user_profile.data = profile_form.cleaned_data.get(data)
            #     user_profile.save
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
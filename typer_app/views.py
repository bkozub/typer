from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import render

from typer_app.forms import UserForm, ProfileForm, CompetitionForm, CompetitionLocationForm


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating


@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
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


@login_required
def create_competition(request):
    if request.method == 'POST':
        comp_form = CompetitionForm(request.POST)
        comp_loc_form = CompetitionLocationForm(request.POST)
        if comp_form.is_valid() and comp_loc_form.is_valid():
            comp_loc_form.save()
            comp_form.instance.competition_location = comp_loc_form.instance
            comp_form.save()
            messages.success(request, ('You created a competition!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        comp_form = CompetitionForm()
        comp_loc_form = CompetitionLocationForm()
    return render(request, 'competition.html', {
        'comp_form': comp_form,
        'comp_loc_form': comp_loc_form
    })


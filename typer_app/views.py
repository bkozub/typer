from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from typer_app.forms import UserForm, ProfileForm, CompetitionForm, CompetitionLocationForm, TypeForm
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
from typer_app.models import Ski_Jumper, Competition, UserProfile, Type
from typer_app.serializers import SkyJumperSerializer, CompetitionSerializer


@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def guide(request):
    return render(request, "how_to.html")


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
            comp_form.instance.location = comp_loc_form.instance
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

@login_required
def type(request):
    if request.method == 'POST':
        type_form = TypeForm(request.POST)
        if type_form.is_valid():
            type_form.instance.user_id = request.user
            # type_form.fields['place'].choices = PLACE_CHOICES
            type_form.save()
            messages.success(request, ('You type a jumper!'))
            return render(request, 'type.html', {
                'type_form': type_form
            })
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        type_form = TypeForm()
    return render(request, 'type.html', {
        'type_form': type_form
    })

# @api_view(['GET'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,TokenAuthentication,))
class JumperViewSet(viewsets.ModelViewSet):
    queryset = Ski_Jumper.objects.all().order_by('pk')
    serializer_class = SkyJumperSerializer

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all().order_by('pk')
    serializer_class = CompetitionSerializer

class UserRankListView(ListView):
    model = UserProfile
    template_name = 'user_rank.html'

    def get_queryset(self):
        return UserProfile.objects.values('user__username','rank').order_by('-rank')

class TypesView(ListView):
    model = Type
    template_name = 'user_types.html'

    def get_queryset(self):
        return Type.objects.filter(user_id=self.request.user)




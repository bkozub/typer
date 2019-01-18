from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from rest_framework import viewsets

from typer_app.forms import CompetitionForm, CompetitionLocationForm, TypeForm, UserForm, ProfileForm
from typer_app.models import Ski_Jumper, Competition, UserProfile, Type, Result
from typer_app.serializers import SkyJumperSerializer, CompetitionSerializer


@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def guide(request):
    return render(request, "how_to.html")


class UpdateProfileView(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
            return self.get(request)


class CreateCompetitionView(View):
    def get(self, request):
        comp_form = CompetitionForm()
        comp_loc_form = CompetitionLocationForm()
        return render(request, 'competition.html', {
            'comp_form': comp_form,
            'comp_loc_form': comp_loc_form
        })

    def post(self, request):
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
            return self.get(request)


class TypeView(FormView):
    template_name = 'type.html'
    form_class = TypeForm
    success_url = reverse_lazy('type')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'type_form': self.get_form(self.form_class)
        })

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.save()
        messages.success(self.request, 'You type a jumper!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return super().form_valid(form)

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
        return UserProfile.objects.values('user__username', 'rank').order_by('-rank')


class UserTypesView(ListView):
    model = Type
    template_name = 'user_types.html'

    def get_queryset(self):
        return Type.objects.filter(user_id=self.request.user)


class CompetitionResultDetailView(ListView):
    model = Result
    template_name = 'competition_result_detail.html'

    def get_queryset(self):
        return Result.objects.filter(competition_id=self.kwargs['pk']).order_by('place')


class CompetitionResultView(ListView):
    model = Result
    template_name = 'competition_result.html'

    def get_queryset(self):
        return Result.objects.all().distinct('competition_id')


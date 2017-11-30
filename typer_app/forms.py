from django.contrib.auth.forms import AuthenticationForm
from django import forms

# If you don't do this you cannot use Bootstrap CSS
from django.contrib.auth.models import User
from django.forms import extras
from django.utils.translation import ugettext_lazy as _
from typer_app.models import UserProfile, Competition, Competition_Location, Type


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'birth_date')
        widgets = {
            'birth_date': extras.SelectDateWidget
        }


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('date','status',)
        widgets = {
            'date': extras.SelectDateWidget
        }


class CompetitionLocationForm(forms.ModelForm):
    class Meta:
        model = Competition_Location
        fields = ('location', 'nationality',)


class TypeForm(forms.ModelForm):
    PLACE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    place = forms.ChoiceField(choices=PLACE_CHOICES)

    # def __init__(self, *args, **kwargs):
    #     no_place = kwargs.get('no_place')
    #     user = kwargs.get('user')
    #     super(TypeForm, self).__init__(*args, **kwargs)
    #     if no_place:
    #         self.fields['place'].choices = PLACE_CHOICES[:-1]

    class Meta:
        model = Type
        fields = ('place', 'comp_id', 'jumpers',)
        labels = {
            'comp_id': _('Competition'),
            'jumpers': _('Jumper')
        }















        # birthdate = forms.DateField(widget=extras.SelectDateWidget)

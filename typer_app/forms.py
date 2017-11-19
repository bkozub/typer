from django.contrib.auth.forms import AuthenticationForm
from django import forms

# If you don't do this you cannot use Bootstrap CSS
from django.contrib.auth.models import User
from django.forms import extras

from typer_app.models import UserProfile, Competition, Competition_Location


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
            'birth_date' : extras.SelectDateWidget
        }

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('comp_date',)
        widgets = {
            'comp_date': extras.SelectDateWidget
        }
class CompetitionLocationForm(forms.ModelForm):
    class Meta:
        model = Competition_Location
        fields = ('location','nationality',)





    # birthdate = forms.DateField(widget=extras.SelectDateWidget)


from django import forms

from .models import Chat
from django.contrib.auth.models import User




####################################################################################

class SingupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    first_name = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "rows": "1",
                "blank": "False"
            }
        )
    )
    last_name = forms.CharField(label="", required=False, widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "rows": "1",
                "null": "True"
            }
        )
    )
    username = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "rows": "1",
            }
        )
    )
    password = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                "placeholder": "Password",
                "rows": "1",
                "type" : "password",
            }
        )
    )

    def clean_first_name(self):
        name = self.cleaned_data.get("first_name")
        name = name.capitalize()
        return name

    def clean_last_name(self):
        lastname = self.cleaned_data.get("last_name")
        lastname = lastname.capitalize()
        return lastname


####################################################################################

class MobileSingupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    first_name = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "rows": "1",
                "blank": "False",
                "class": "input"

            }
        )
    )
    last_name = forms.CharField(label="", required=False, widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "rows": "1",
                "null": "True",
                "class": "input"
            }
        )
    )
    username = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "rows": "1",
                "class": "input"
            }
        )
    )
    password = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                "placeholder": "Password",
                "rows": "1",
                "type" : "password",
                "class": "input"
            }
        )
    )

    def clean_first_name(self):
        name = self.cleaned_data.get("first_name")
        name = name.capitalize()
        return name

    def clean_last_name(self):
        lastname = self.cleaned_data.get("last_name")
        lastname = lastname.capitalize()
        return lastname

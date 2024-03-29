from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Counselee, Network


class CounseleeRegisterForm(forms.ModelForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Counselee
        fields = ['username', 'password1', 'password2', 'firstname', 'lastname', 'othernames', 'date_of_birth',
                  'gender', 'phone_number', 'network', 'email', 'hometown']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['network'].queryset = Network.objects.all()

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            counselee = super().save(commit=False)
            counselee.set_password(self.cleaned_data["password1"])
            if commit:
                counselee.save()
            return counselee


class CounseleeUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Counselee
        fields = ['username', 'email']


class CounseleePictureForm(forms.ModelForm):
    class Meta:
        model = Counselee
        fields = ['image']

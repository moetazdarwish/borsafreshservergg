from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.models import User
from django.forms import ModelForm
import json
from profils.models import UsersProfiles


class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'email','username','first_name','last_name','password1','password2']

    # def save(self, commit=True):
    #     user = super(CreateUser, self).save(commit=False)
    #     user.username = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #
    #     return user

class UserProfileForm(ModelForm):

    class Meta:
        model = UsersProfiles
        fields = [ 'phone','address','city','country','area']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

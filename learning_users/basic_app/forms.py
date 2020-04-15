from django import forms
from django.contrib.auth.models import User  #default
from basic_app.models import UserProfileInfo # we created


# this is the default 'User'
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) ## we need to modify password field

    ## we define the 'UserForm' class inside the inner meta class
    #https://www.quora.com/Why-do-we-use-the-class-Meta-inside-the-ModelForm-in-Django
    class Meta():
        model = User
        fields = ('username','email','password')

## customized user
class UserProfileInfoForm(forms.ModelForm):
    
    class Meta():
        model = UserProfileInfo
        fields  = ('portfolio_site','profile_pic')

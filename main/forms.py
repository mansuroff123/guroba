from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput, TextInput

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(max_length=125,
                             widget=forms.EmailInput(
                                 attrs={'class': 'box', 'placeholder': 'Enter Your Email'}),
                             label=False, required=True,)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Confirm'}))
 
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		widgets = {
        'username': TextInput(attrs={
            'class': "box",
            'placeholder': "Enter Your Username",
            'id' : "id_username", 
        })
        }
        




	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailInput, PasswordInput, TextInput

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)


	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		# widgets = {
        # 'username': TextInput(attrs={
        #     'class': "form-control text-lg h-8 rounded-full px-2 pt-1 border-2 border-black",
        #     'placeholder': "Username",
        #     'id' : "id_register_form_username" , 
        # }),
        # 'email': EmailInput(attrs={
        #     'class': "form-control text-lg h-8 rounded-full px-2 pt-1 border-2 border-black",
        #     'placeholder': 'Email address' ,
        #     'id' : 'id_email' , 
        # }),
        # 'password1': PasswordInput(attrs={
        #     'class': "form-control text-lg h-8 rounded-full px-2 pt-1 border-2 border-black",
        #     'type': 'password',
        #     'name': 'password',
        #     'placeholder': 'Password',
        #     'id' : "id_register_form_password1", 
        # }),
        # 'password2': PasswordInput(attrs={
        #     'class': "form-control text-lg h-8 rounded-full px-2 pt-1 border-2 border-black",
        #     'placeholder': 'Password',
        #     'id' : "id_register_form_password2" , 
        # }),
    	# }




	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

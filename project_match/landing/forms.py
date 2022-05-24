from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser

class CreateAppUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form_element in self.visible_fields():
            form_element.field.widget.attrs['class'] = 'form-control form-control-lg'
    
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(required=True)
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()

    class Meta:
        model = AppUser
        fields=('first_name','last_name','email','password1','password2')

    def clean(self):
        self.cleaned_data = super(CreateAppUserForm, self).clean()
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        return self.cleaned_data
    
    def save(self):
        self.fields['username'] = self.fields['email']
        user = AppUser( first_name = self.cleaned_data.get('first_name'), 
                        last_name = self.cleaned_data.get('last_name'),
                        username = self.cleaned_data.get('email'),
                        email = self.cleaned_data.get('email'),
                        password = self.cleaned_data.get('password1')
                         )
        AppUser.save(user)
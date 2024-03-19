from django.contrib.auth.models import User
from django import forms



class LoginForm(forms.Form):
    username=forms.CharField(required=True, widget=forms.TextInput())
    password=forms.CharField(required=True, widget=forms.PasswordInput())

   
        
class RegisterForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):

        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password_confirm']=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password')

    def clean_confirm_password(self):
        password=self.cleaned_data['password']
        password_confirm=self.cleaned_data['password_confirm']

        if password_confirm != password:
            raise forms.ValidationError('passwordlar bir xil bolishi lozim')

        return password

    def clean_username(self):
        username=self.cleaned_data['username']

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan kichik va 30 dan katta bolmasligi lozim')
        
        return username
        


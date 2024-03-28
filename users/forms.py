from users.models import User
from django import forms


class ProfileForm(forms.ModelForm):
   
    first_name=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control "}))
    last_name=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField( widget=forms.EmailInput(attrs={"class":"form-control"}))
    photo=forms.ImageField( widget=forms.FileInput(attrs={"class":"form-control"}))
     
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username',  'email', 'phone_number', 'photo' )
        
class LoginForm(forms.Form):
    username=forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control  "}))
    password=forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control "}))

    def clean_username(self):
        username=self.cleaned_data['username']

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan kichik va 30 dan katta bolmasligi lozim')
        
        return username
        
class RegisterForm(forms.ModelForm):
    first_name=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control "}))
    last_name=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField( widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password=forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    def __init__(self, *args, **kwargs):

        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['confirm_password']=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('passwordlar bir xil bolishi lozim')

        return password

    def clean_username(self):
        username=self.cleaned_data['username']

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan kichik va 30 dan katta bolmasligi lozim')
        
        return username
        


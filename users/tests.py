from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm
from django import forms

# Create your tests here.
 
class RegisterTestCase(TestCase):
    
    def test_register_page(self):
        self.client.post(
            reverse('users:register_page'),
            data={
                'username':'ilyosbek',
                'first_name':'Asadbek',
                'last_name':'Sotvoldiyev',
                'email':'asadbek@gmail.com',
                'password':'1234',
                'password_confirm':'1234'

            }
        )

        user_count=User.objects.all().count()

        user=User.objects.get(username='ilyosbek')


        self.assertEqual(user_count, 1)
        self.assertEqual(user.first_name, 'Asadbek')
        self.assertEqual(user.last_name, 'Sotvoldiyev' )
        self.assertEqual(user.email, 'asadbek@gmail.com')
        self.assertNotEqual(user.password, '1234')
        self.assertTrue(user.check_password("1234"))
 

    
 
class TestLoginForm(TestCase):
    def test_login_page(self):
       form = LoginForm()
       self.assertEqual(form.fields['username'].required, True)
       self.assertEqual(form.fields['password'].required, True)
       self.assertIsInstance(form.fields['username'].widget, forms.TextInput)
       self.assertIsInstance(form.fields['password'].widget, forms.PasswordInput)      
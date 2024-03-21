from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from .forms import LoginForm, RegisterForm
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
                'password':'12345',
                'confirm_password':'12345'

            }
        )

        user_count=User.objects.all().count()

        user=User.objects.get(username='ilyosbek')

        
        self.assertEqual(user_count, 1)
        self.assertEqual(user.first_name, 'Asadbek')
        self.assertEqual(user.last_name, 'Sotvoldiyev' )
        self.assertEqual(user.email, 'asadbek@gmail.com')
        self.assertNotEqual(user.password, '12345')
        self.assertTrue(user.check_password("12345"))
 

    
    def test_clean_username (self):

        response= self.client.post(
            reverse('users:register_page'),
            data={
                'username':'root',
                'first_name':'Asadbek',
                'last_name':'Sotvoldiyev',
                'email':'asadbek@gmail.com',
                'password':'1234',
                'confirm_password':'1234'

            }
        )
        form=response.context['form']
        user_count=User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors, 1)
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'], ['username uzunligi 5 dan kichik va 30 dan katta bolmasligi lozim'])

    def test_password_field (self):

        response= self.client.post(
            reverse('users:register_page'),
            data={
                'username':'ilyosbek',
                'first_name':'Asadbek',
                'last_name':'Sotvoldiyev',
                'email':'asadbek@gmail.com',
                'password':'12345',
                'confirm_password':'1234'

            }
        )
        form=response.context['form']
        user_count=User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn('confirm_password', form.errors.keys())
        self.assertEqual(form.errors['confirm_password'], ['passwordlar bir xil bolishi lozim'])

        # Enter a valid email address.
    def test_email_field (self):

        response= self.client.post(
            reverse('users:register_page'),
            data={
                'username':'ilyosbek',
                'first_name':'Asadbek',
                'last_name':'Sotvoldiyev',
                'email':'asadbek@gm',
                'password':'12345',
                'confirm_password':'12345'

            }
        )
        form=response.context['form']
        user_count=User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

    # A user with that username already exists.

   
                
    def test_user_field (self):
        
        self.user = User.objects.create_user(username='ilyosbek', email='asadbek@gmail.com', password='password123')
        
        data={
                'username':'ilyosbek',
                'first_name':'Asadbek',
                'last_name':'Sotvoldiyev',
                'email':'asadbek@gmail.com',
                'password':'12345',
                'confirm_password':'12345'

            }
        form=RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue('username' in form.errors)
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])

class LoginTestCase(TestCase):

    def test_login_success(self):
        user = User.objects.create_user(username='ilyosbek', email='asadbek@gmail.com', password='password123')
        user.set_password('password123')

        user.save()

        self.client.post(
            reverse('users:login_page'),
            data={
                'username':'ilyosbek',
                'password':'password123',

            }
        )

        user_count=User.objects.count()
        self.assertEqual(user_count, 1)
        user=get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_clean_username (self):

        response= self.client.post(
            reverse('users:register_page'),
            data={
                'username':'root',
                'first_name':'Asadbek',
                'last_name':'Sotvoldiyev',
                'email':'asadbek@gmail.com',
                'password':'1234',
                'confirm_password':'1234'

            }
        )
        form=response.context['form']
        user_count=User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors, 1)
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'], ['username uzunligi 5 dan kichik va 30 dan katta bolmasligi lozim'])

class LogoutTestCase(TestCase):

    def test_login_success(self):
        user = User.objects.create_user(username='ilyosbek', email='asadbek@gmail.com', password='password123')
        user.set_password('password123')
        user.save()
        
        user=get_user(self.client)
        self.assertFalse(user.is_authenticated)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False, initial='test@example.com')
    phone_number = forms.CharField(max_length=15, required=False, initial='1234567890')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

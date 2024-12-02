from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields  = ['username', 'email', 'password', 'password_confirm']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        # Check if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        email = cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists!")
        return cleaned_data
    
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password.")
        return cleaned_data

class ReserveParkingForm(forms.Form):
    vehicle_number = forms.CharField(max_length=20)
    registration_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    is_regular_customer = forms.BooleanField(required=False)
    contact_number = forms.CharField(max_length=20)
    
# myapp/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, House, ApartmentVisit
from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name']

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['city', 'street', 'house_number', 'entrances', 'apartments_per_entrance']






class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    birth_date = forms.DateField(required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth_date', 'address', 'gender')




class ApartmentVisitForm(forms.ModelForm):
    class Meta:
        model = ApartmentVisit
        fields = ['apartment_number', 'door_opened', 'date', 'time', 'reaction', 'contact_name', 'contact_phone', 'comment']
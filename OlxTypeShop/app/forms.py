from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from app.models import *


class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateMyCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number']


class AddOfferForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['added_by', 'slug', 'created', 'updated']

from django import forms
from django.db.models import fields
from .models import EMPLOYEE, TRIP


class RegisterDriverForm(forms.ModelForm):
    class Meta:
        model = EMPLOYEE
        fields = '__all__'

class SearchEmployeeForm(forms.Form):
    CNIC = forms.CharField(label="CNIC", max_length=15)

class EmployeeUpdateForm(forms.ModelForm):
    CNIC =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    class Meta:
        model = EMPLOYEE
        fields = '__all__'
        exclude = ['available']

class BookCustomTripForm(forms.ModelForm):
    class Meta:
        model = TRIP
        fields = '__all__'
        exclude = ['is_custom']
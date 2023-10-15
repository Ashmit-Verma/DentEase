from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator
from django.db import transaction
from .models import User
from .models import Denstist




class dentistForm(UserCreationForm):
    full_name=forms.CharField(max_length=100,label='full name')
    email = forms.EmailField(max_length=150, label='Email')
    registration_number = forms.CharField(max_length=50,label='Registration number')
    contact = forms.IntegerField(label='Contact No.', validators=[MaxValueValidator(9999999999)])
    clinic_address = forms.CharField(max_length=100,label='Clinic Address')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('full_name','email','registration_number','contact','clinic_address','password1', 'password2',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dentist = True
        user.save()
        dentist = Denstist.objects.create(user=user)
        dentist.email=self.cleaned_data.get('email')
        dentist.registration_number=self.cleaned_data.get('registration_number')
        dentist.clinicAddress=self.cleaned_data.get('clinic_address')
        dentist.contact=self.cleaned_data.get('contact')
        dentist.save()
        return user
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'locality', 'message']

from django import forms

from poplar.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person


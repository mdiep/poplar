
from datetime import datetime

from django import forms

from poplar.models import Person, Note

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('author', 'subject', 'timestamp')
    
    def __init__(self, *args, **kwargs):
        if 'author' in kwargs:
            self._author = kwargs.pop('author')
        if 'subject' in kwargs:
            self._subject = kwargs.pop('subject')
        super(NoteForm, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        obj = super(NoteForm, self).save(commit=False)
        obj.author  = self._author
        obj.subject = self._subject
        if not obj.timestamp:
            obj.timestamp = datetime.now()
        if commit:
            obj.save()
        return obj

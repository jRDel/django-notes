from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'size': '40'}))
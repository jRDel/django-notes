from django.db import models
from django import forms
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    def __str__(self):
        return self.title
    def get_description(self):
        return self.description
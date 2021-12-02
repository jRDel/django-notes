from django.db import models
from django import forms
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=254, blank=True)
    def __str__(self):
        return self.title
    def get_description(self):
        return self.description
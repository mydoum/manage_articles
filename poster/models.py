from django.db import models
from django import forms
from django.forms import RadioSelect


class CreateArticle(forms.Form):
    name = forms.CharField(max_length=250)
    description = forms.TextInput()
#    type_of_article = (
#        ('AR', 'Article'),
#        ('IN', 'Incident'),
#        ('RE', 'Ressource'),
#        ('DI', 'Discussion'),
#    )
#    category = forms.ChoiceField(widget=RadioSelect, choices=type_of_article)

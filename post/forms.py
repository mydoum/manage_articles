from django import forms
from index.models import Article

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'description',)
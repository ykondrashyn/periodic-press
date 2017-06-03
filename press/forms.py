__author__ = 'jujbob'

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'faculty', 'atype', 'link', 'created_date')

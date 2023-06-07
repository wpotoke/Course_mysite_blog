from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=SummernoteWidget())  # new

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField()

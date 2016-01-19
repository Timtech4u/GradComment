from django import forms
from GradComment.models import Comments


class CommentsForm(forms.ModelForm):
    comments = forms.Textarea(attrs={'class': 'textarea'})

    class Meta:
        model = Comments
        fields = ['comment_text']


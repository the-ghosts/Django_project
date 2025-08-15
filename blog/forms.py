from django import forms
from .models import PostModel, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = PostModel
        fields=('title', 'content')

class PostEditForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields=('title', 'content')


class CommentForm(forms.ModelForm):
        comments = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Comment'}))
        class Meta:
            model = Comment
            fields= ('comments',)

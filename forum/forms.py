from django import forms
from .models import Comment, Discussion


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['visible'].initial = True

    class Meta:
        model = Comment
        fields = ('body', 'visible')
        labels = {'body': 'Your comment', }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'visible': forms.HiddenInput,
        }


class ForumNewTopic(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ForumNewTopic, self).__init__(*args, **kwargs)
        self.fields['visible'].initial = True
        self.fields['premium_only'].initial = False

    class Meta:
        model = Discussion
        fields = {
            'picture',
            'title',
            'body',
            'forum',
            'poster',
            'premium_only',
            'visible',
        }
        widgets = {
            'picture': forms.FileInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'premium_only': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
                ),
            'visible': forms.HiddenInput(),
        }


class Discussion_Edit_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Discussion_Edit_Form, self).__init__(*args, **kwargs)
        self.fields['visible'].initial = True
        self.fields['premium_only'].initial = False

    class Meta:
        model = Discussion
        fields = {
            'picture',
            'title',
            'body',
            'forum',
            'poster',
            'premium_only',
            'visible',
        }
        widgets = {
            'picture': forms.FileInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'forum': forms.HiddenInput(),
            'premium_only': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
                ),
            'visible': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
                ),
        }

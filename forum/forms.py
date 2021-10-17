from django import forms
from .models import Comment


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
            # 'discussion': forms.HiddenInput,
            'visible': forms.HiddenInput,
        }

from django import forms
from .widgets import CustomClearableFileInput
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
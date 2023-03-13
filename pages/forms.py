from django import forms
from .models import Post

# Reordering Form and View


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=250)

    class Meta:
        model = Post
        fields = ("title",)

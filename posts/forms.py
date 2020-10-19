from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    # title = forms.CharField(max_length=100,
    #                         required=True)
    # content = forms.CharField(widget=forms.Textarea,
    #                           required=False)
    # status = forms.BooleanField(label='Publish',
    #                             required=False)

    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'status']

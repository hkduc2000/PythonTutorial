from django import forms
from tutorialsite.models import Post, Comment, Tag, Exercise


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('tag', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class:': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent border border-primary',
                                          'style': 'min-height:300px;'}),
        }


class CommentForm(forms.ModelForm):
    class Meta():
      model = Comment
      fields = ('author', 'text')

      widgets = {
          'author': forms.TextInput(attrs={'class': 'textinputclass'}),
          'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent border border-primary',
                                        'style': 'min-height:300px;'}),
      }


class ExerciseForm(forms.ModelForm):

    class Meta():
        model = Exercise
        fields = ('post','title', 'text', 'solution')

        widgets = {
            'title': forms.TextInput(attrs={'class:': 'textinputclass', 'style': 'min-width:700px;'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent border border-primary',
                                              'style': 'min-height:300px;'}),
            'solution': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent border border-primary',
                                          'style': 'min-height:300px;'}),
        }

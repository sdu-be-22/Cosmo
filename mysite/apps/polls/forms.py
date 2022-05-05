from django import forms
from .models import Post, Category, Comment

choices = [('Work', 'Work'),
           ('Education', 'Education'),
           ('Home and lifestyle', 'Home and lifestyle'),
           ('Family', 'Family'),
           ('Journey', 'Journey'),
           ('Interests and hobbies', 'Interests and hobbies'),
           ('Health and well-being', 'Health and well-being'),
           ('Important events and achievements', 'Important events and achievements'),
           ('Honoring the memory', 'Honoring the memory'), ]


# choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # 'placeholder': 'This is Title Placeholder Stuff'
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'placeholder': 'This is Title Placeholder Stuff'
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body')

        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'comment'}),
            # 'placeholder': 'This is Title Placeholder Stuff'
            'body': forms.Textarea(attrs={'class': 'comment'}),
        }

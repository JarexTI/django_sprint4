from django import forms

from .models import Comment, Post, User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")


class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("author",)
        widgets = {
            "text": forms.Textarea({"rows": "5"}),
        }


class CommentEditForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": forms.Textarea({"rows": "3"})
        }

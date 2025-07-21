from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # ⬅️ This is critical

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

from django import forms
from .models import Blog
from .models import Notice

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'category', 'priority', 'start_date', 'end_date', 'target_audience', 'attachment', 'tags']
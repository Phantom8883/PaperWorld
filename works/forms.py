from django import forms
from .models import Work



class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
from django import forms
from .models import JobHistory, EduHistory

class JobHistoryForm(forms.ModelForm):
    date_start = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'datepicker', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )
    date_end = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'datepicker', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = JobHistory
        fields = ['company', 'title', 'description', 'date_start', 'date_end']

    
class EduHistoryForm(forms.ModelForm):
    date_start = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'datepicker', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )
    date_end = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'datepicker', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = EduHistory
        fields = ['name_school', 'name_major', 'date_start', 'date_end']

from django import forms
from .models import JobHistory, EduHistory, Company
from django.contrib.auth.models import User

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


class AddOwnersForm(forms.ModelForm):
    new_owners = forms.ModelMultipleChoiceField(queryset=User.objects.none(), required=True)

    class Meta:
        model = Company
        fields = []

    def __init__(self, *args, **kwargs):
        owners_queryset = kwargs.pop('owners_queryset', User.objects.none())
        super(AddOwnersForm, self).__init__(*args, **kwargs)
        self.fields['new_owners'].queryset = owners_queryset
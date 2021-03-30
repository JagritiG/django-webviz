from django import forms
from .models import Csv


class UploadCsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('title', 'csv')



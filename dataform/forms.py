from django import forms
from .models import DataframeNode

class DataframeForm(forms.ModelForm):
 class Meta:
  model = DataframeNode
  fields = ('tiff_file', 'gtiff_file',)
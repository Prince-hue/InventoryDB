from django import forms
from .models import inout
from .models import Asset
#from dal import autocomplete

class inoutforms(forms.ModelForm):
    class Meta:
        model = inout
        fields = '__all__'
        #fields = ['user', 'address']
        
class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name_of_asset', 'quantity', 'name_of_person']
        #widgets = {
        #    'name_of_asset': autocomplete.ModelSelect2(url='asset-autocomplete')
        #}
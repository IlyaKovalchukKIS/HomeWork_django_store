from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'preview', 'category', 'price', 'date_creation', 'date_last_change']

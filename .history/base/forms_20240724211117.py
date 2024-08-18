from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'description', 'sku', 'price_paid', 'price_sold', 'apparel_size' ,'size', 'condition', 'quantity', 'category']

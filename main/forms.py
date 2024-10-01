from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'type', 'sound_profile', 'image']
        # Tidak ada widget khusus untuk type dan sound_profile

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['sound_profile'].widget = forms.Select(choices=[])

    class Media:
        js = ('js/product_form.js',)
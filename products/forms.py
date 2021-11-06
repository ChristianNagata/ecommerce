from django import forms


class ClotheForm(forms.Form):
    SIZES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    ]
    clothe_size = forms.CharField(
        label=False, max_length=2, widget=forms.RadioSelect(choices=SIZES))

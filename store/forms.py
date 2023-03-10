from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=5)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField(required=False)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, min_length=1)
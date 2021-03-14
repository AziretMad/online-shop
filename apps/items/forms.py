from django import forms
from .models import Category


class CategoryForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Категории"
    )

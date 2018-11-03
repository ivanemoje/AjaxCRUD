from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'installation_date', 'account_manager', 'monthly_charge', 'capacity', 'service_type', )

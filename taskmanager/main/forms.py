from django import forms


class UserForm(forms.Form):
    cardNumber = forms.CharField(label='Номер карти', required=True, min_length=4, max_length=4)
    password = forms.CharField(label='PIN-код', required=True, min_length=4, max_length=4)

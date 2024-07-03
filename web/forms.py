from django import forms


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Email')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    customer_lastname = forms.CharField(max_length=64, label='Apellido')
    message = forms.CharField(label='Mensaje')
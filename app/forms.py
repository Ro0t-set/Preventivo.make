from django import forms
from django.db import models
from .models import Cliente, Preventivo, Prestazione

class PrestazioneForm(forms.ModelForm):
        class Meta:
            model = Prestazione
            fields = ('prestazioni', 'prezzo')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'cognome', 'telefono', 'codice_fiscale', 'mail', 'note')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
            'codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),

        }


class PreventivoForm(forms.ModelForm):
    class Meta:
        model = Preventivo
        fields = ['cliente','prestazione1', 'ripetizione1', 'prestazione2', 'ripetizione2', 'prestazione3', 'ripetizione3', 'prestazione4', 'ripetizione4', 'prestazione5', 'ripetizione5']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'custom-select col-4'}),
            'prestazione1': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione2': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione3': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione4': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione5': forms.Select(attrs={'class': 'form-control col-4'}),
            'ripetizione1': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione2': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione3': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione4': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione5': forms.NumberInput(attrs={'class': 'form-control col-2'}),


        }


        #ripetizione= forms.NumberInput()

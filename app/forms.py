from django import forms
from django.db import models
from .models import Cliente, Preventivo, Prestazione

class PrestazioneForm(forms.ModelForm):
        class Meta:
            model = Prestazione
            fields = ('prestazioni', 'prezzo')
        widgets = {
            'prestazione': forms.TextInput(attrs={'class': 'form-control'}),
            'prezzo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'cognome', 'telefono','indirizzo', 'codice_fiscale', 'mail', 'note')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'indirizzo': forms.TextInput(attrs={'class': 'form-control'}),
            'codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
            'codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),

        }


class PreventivoForm(forms.ModelForm):
    prestazione1 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione2 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione3 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione4 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione5 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione6 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione7 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione8 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione9 = forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione10= forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione11= forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione12= forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione13= forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione14= forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))
    prestazione15= forms.ModelChoiceField(queryset=Prestazione.objects.order_by('prestazioni'))

    class Meta:
        model = Preventivo
        fields = ['cliente','prestazione1', 'ripetizione1', 'prestazione2', 'ripetizione2', 'prestazione3', 'ripetizione3', 'prestazione4', 'ripetizione4', 'prestazione5', 'ripetizione5', 'prestazione6', 'ripetizione6', 'prestazione7', 'ripetizione7', 'prestazione8', 'ripetizione8', 'prestazione9', 'ripetizione9',
         'prestazione10', 'ripetizione10', 'prestazione11', 'ripetizione11', 'prestazione12', 'ripetizione12', 'prestazione13', 'ripetizione13', 'prestazione14', 'ripetizione14', 'prestazione15', 'ripetizione15']

        widgets = {
            'cliente': forms.Select(attrs={'class': 'custom-select col-4'}),
            'prestazione1': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione2': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione3': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione4': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione5': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione6': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione7': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione8': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione9': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione10': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione11': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione12': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione13': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione14': forms.Select(attrs={'class': 'form-control col-4'}),
            'prestazione15': forms.Select(attrs={'class': 'form-control col-4'}),
            'ripetizione1': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione2': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione3': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione4': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione5': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione6': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione7': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione8': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione9': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione10': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione11': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione12': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione13': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione14': forms.NumberInput(attrs={'class': 'form-control col-2'}),
            'ripetizione15': forms.NumberInput(attrs={'class': 'form-control col-2'}),



        }




        #ripetizione= forms.NumberInput()

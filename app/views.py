from django.shortcuts import render
from django.utils import timezone
from .models import Prestazione, Preventivo, Cliente
from django.shortcuts import render, get_object_or_404
from .forms import ClienteForm, PreventivoForm, PrestazioneForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import operator
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


# Create your views here.

def home(request):


    return render(request, 'home.html', {})

def utente(request):
    utenti= Cliente.objects.order_by('cognome')

    return render(request, 'utente.html', {'utenti':utenti})

def add_utente(request):
    if request.method == "POST":
            form = ClienteForm(request.POST)
            if form.is_valid():
                cliente = form.save(commit=False)
                cliente.published_date = timezone.now()
                cliente.save()
                return HttpResponseRedirect('/utente')

    else:
        form = ClienteForm()

    return render(request, 'add_utente.html', {'form':form})

def prestazione(request):
    prestazioni= Prestazione.objects.order_by('prestazioni')

    return render(request, 'prestazione.html', {'prestazioni':prestazioni})

def edit_utente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
                cliente = form.save(commit=False)
                cliente.published_date = timezone.now()
                cliente.save()
                return HttpResponseRedirect('/utente')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'utente_edit.html', {'form': form, 'cliente':cliente})


def add_prestazione(request):
    if request.method == "POST":
            form = PrestazioneForm(request.POST)
            if form.is_valid():
                prestazione = form.save(commit=False)
                prestazione.published_date = timezone.now()
                prestazione.save()
                return HttpResponseRedirect('/prestazione')

    else:
        form = PrestazioneForm()

    return render(request, 'add_prestazione.html', {'form':form})



def edit_prestazione(request, pk):
    prestazione = get_object_or_404(Prestazione, pk=pk)
    if request.method == "POST":
        form = PrestazioneForm(request.POST, instance=prestazione)
        if form.is_valid():
                prestazione = form.save(commit=False)
                prestazione.published_date = timezone.now()
                prestazione.save()
                return HttpResponseRedirect('/prestazione')
    else:
        form = PrestazioneForm(instance=prestazione)
    return render(request, 'prestazione_edit.html', {'form': form, 'prestazione':prestazione})


def preventivo(request):

    preventivo= Preventivo.objects.order_by('-published_date')



    return render(request, 'preventivo.html', {'preventivo':preventivo})



def add_preventivo(request):

    form= PreventivoForm(request.POST)

    if request.method == "POST":
        if form.is_valid():


                if form.is_valid():
                    preventivo = form.save(commit=False)
                    preventivo.published_date = timezone.now()
                    preventivo.save()
                    print(form.as_table())
                    return HttpResponseRedirect('/preventivo')

    else:
        form= PreventivoForm()


    return render(request, 'add_preventivo.html', {'form':form})



def stampa_preventivo(request, pk):
    preventivo = get_object_or_404(Preventivo, pk=pk)
    tot1= int(preventivo.ripetizione1  * preventivo.prestazione1.prezzo)
    tot2= int(preventivo.ripetizione2  * preventivo.prestazione2.prezzo)
    tot3= int(preventivo.ripetizione3  * preventivo.prestazione3.prezzo)
    tot4= int(preventivo.ripetizione4  * preventivo.prestazione4.prezzo)
    tot5= int(preventivo.ripetizione5  * preventivo.prestazione5.prezzo)
    tot6= int(preventivo.ripetizione6  * preventivo.prestazione6.prezzo)
    tot7= int(preventivo.ripetizione7  * preventivo.prestazione7.prezzo)
    tot8= int(preventivo.ripetizione8  * preventivo.prestazione8.prezzo)
    tot9= int(preventivo.ripetizione9  * preventivo.prestazione9.prezzo)
    tot10= int(preventivo.ripetizione10  * preventivo.prestazione10.prezzo)
    tot11= int(preventivo.ripetizione11  * preventivo.prestazione11.prezzo)
    tot12= int(preventivo.ripetizione12  * preventivo.prestazione12.prezzo)
    tot13= int(preventivo.ripetizione13  * preventivo.prestazione13.prezzo)
    tot14= int(preventivo.ripetizione14  * preventivo.prestazione14.prezzo)
    tot15= int(preventivo.ripetizione15  * preventivo.prestazione15.prezzo)


    tot=[tot1,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15]

    totoale=tot1 + tot2 + tot3 + tot4 +tot5 + tot6 + tot7 + tot8 + tot9 + tot10 + tot11 + tot12 + tot13 + tot14 + tot15


    return render(request, 'stampa_preventivo.html', { 'preventivo':preventivo, 'tot':tot, 'totoale':totoale})




def edit_preventivo(request, pk):
    preventivo = get_object_or_404(Preventivo, pk=pk)
    if request.method == "POST":
        form = PreventivoForm(request.POST, instance=preventivo)
        if form.is_valid():
                preventivo = form.save(commit=False)
                preventivo.published_date = timezone.now()
                preventivo.save()
                return HttpResponseRedirect('/preventivo')
    else:
        form = PreventivoForm(instance=preventivo)
    return render(request, 'preventivo_edit.html', {'form': form, 'preventivo':preventivo})

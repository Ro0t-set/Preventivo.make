from django.shortcuts import render
from django.utils import timezone
from .models import Prestazione, Preventivo, Cliente
from django.shortcuts import render, get_object_or_404
from .forms import ClienteForm, PreventivoForm
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
                    preventivo.prezzo= int((preventivo.ripetizione1 * preventivo.prestazione1.prezzo) + (preventivo.ripetizione2 * preventivo.prestazione2.prezzo) + (preventivo.ripetizione3 * preventivo.prestazione3.prezzo) + (preventivo.ripetizione4 * preventivo.prestazione4.prezzo) + (preventivo.ripetizione5 * preventivo.prestazione5.prezzo))
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

    tot=[tot1,tot2,tot3,tot4,tot5]

    return render(request, 'stampa_preventivo.html', { 'preventivo':preventivo, 'tot':tot})




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

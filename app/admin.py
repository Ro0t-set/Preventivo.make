from django.contrib import admin
from .models import Preventivo, Prestazione, Cliente


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Prestazione)
admin.site.register(Preventivo)

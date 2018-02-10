from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your models here.

class Prestazione(models.Model):
    prestazioni= models.CharField(max_length=100, default="")
    prezzo= models.IntegerField(default=0)
    def __str__(self):
        return str(self.prestazioni)

class Cliente(models.Model):
    nome= models.CharField(max_length=100, default="",blank=True, null=True)
    cognome= models.CharField(max_length=100, default="",blank=True, null=True)
    telefono= models.CharField(max_length=100, default="",blank=True, null=True)
    indirizzo= models.CharField(max_length=100, default="",blank=True, null=True)
    note= models.TextField(max_length=1000, default="",blank=True, null=True)
    codice_fiscale= models.CharField(max_length=100, default="",blank=True, null=True)
    mail= models.EmailField(max_length=100, default="",blank=True, null=True)



    def __str__(self):
        return str(self.cognome)



class Preventivo(models.Model):
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)

    prestazione1 = models.ForeignKey('Prestazione',on_delete=models.CASCADE, related_name="prestazione1")
    ripetizione1 = models.IntegerField(default=1)

    prestazione2 = models.ForeignKey('Prestazione',on_delete=models.CASCADE, related_name="prestazione2", default=3, blank=True, null=True)
    ripetizione2 = models.IntegerField(default=1)

    prestazione3 = models.ForeignKey('Prestazione',on_delete=models.CASCADE, related_name="prestazione3", default=3, blank=True, null=True)
    ripetizione3 = models.IntegerField(default=1)

    prestazione4 = models.ForeignKey('Prestazione',on_delete=models.CASCADE, related_name="prestazione4", default=3, blank=True, null=True)
    ripetizione4 = models.IntegerField(default=1)

    prestazione5 = models.ForeignKey('Prestazione',on_delete=models.CASCADE, related_name="prestazione5", default=3, blank=True, null=True)
    ripetizione5 = models.IntegerField(default=1)

    prezzo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cliente)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

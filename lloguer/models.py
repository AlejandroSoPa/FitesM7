from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    
    def __str__(self):
        return self.matricula + ' - ' + self.marca + " " + self.model

class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inici = models.DateField()
    data_fi = models.DateField()
    
    def __str__(self):
        return self.automobil.matricula + ' - ' + self.usuari.username + ' - ' + str(self.data_inici) + ' - ' + str(self.data_fi)
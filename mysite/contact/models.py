from django.db import models
import datetime


# Create your models here.
class Anfrage(models.Model):
    name = models.CharField(max_length=70)
    betreff = models.CharField(max_length=70)
    handy = models.IntegerField()
    von = models.CharField(max_length=70)
    nach = models.CharField(max_length=70)
    abholzeit = models.CharField(max_length=70)
    bestellzeit = models.CharField(max_length=70, default=datetime.datetime.now())
    anmerkung = models.CharField(max_length=140, blank=True)

    def _str_(self):
        return str(self.abholzeit) + ' ' + self.name + ' ' + self.von + ' ' + self.nach + ' ' + self.handy + ' ' + self.bestellzeit + ' ' + self.anmerkung
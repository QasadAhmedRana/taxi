from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# SQL Table for Bestellung
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
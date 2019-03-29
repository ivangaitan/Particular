# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Distrito (models.Model):
    nom = models.CharField(max_length = 50)

class Candidato (models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 50)
    edad = models.SmallIntegerField(null=False)
    distrito = models.ForeignKey(Distrito)

class Voto (models.Model):
    valido = models.BooleanField(default=True)
    candidato = models.ForeignKey(Candidato)





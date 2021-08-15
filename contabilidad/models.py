from django.db import models
from django.contrib import admin
from django.apps import apps
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class C110(models.Model):
	codigo = models.CharField(blank=True,max_length=12)
	nombre = models.CharField(blank=True,max_length=65)
	movimiento = models.BooleanField(blank=True,help_text='',verbose_name='')
	nivel = models.CharField(blank=True,max_length=1)
	tipomoneda = models.CharField(blank=True,max_length=3)
	asienautom = models.BooleanField(blank=True,help_text='',verbose_name='')
	ctacargo = models.CharField(blank=True,max_length=12)
	ctaabono = models.CharField(blank=True,max_length=12)
	validrefer = models.CharField(blank=True,max_length=1)
	validproy = models.CharField(blank=True,max_length=1)
	validcas = models.CharField(blank=True,max_length=1)
	validdoc = models.CharField(blank=True,max_length=1)
	codant = models.CharField(blank=True,max_length=15)
	oficin = models.CharField(blank=True,max_length=5)
	banco = models.CharField(blank=True,max_length=3)
	tipocta = models.CharField(blank=True,max_length=10)
	cuentbanca = models.CharField(blank=True,max_length=25)
	descta1 = models.CharField(blank=True,max_length=60)
	descta2 = models.CharField(blank=True,max_length=60)
	descta3 = models.CharField(blank=True,max_length=60)
	descta4 = models.CharField(blank=True,max_length=60)
	descta5 = models.CharField(blank=True,max_length=60)
	descta6 = models.CharField(blank=True,max_length=60)
	codproy = models.CharField(blank=True,max_length=10)
	feccre = models.DateTimeField(blank=True, null=False,help_text='',verbose_name='')
	fecmod = models.DateTimeField(blank=True, null=False,help_text='',verbose_name='')
	feceli = models.DateTimeField(blank=True, null=False,help_text='',verbose_name='')
	idusu = models.CharField(blank=True,max_length=10)
	cierre = models.PositiveSmallIntegerField()
	nyear = models.PositiveSmallIntegerField()
	nmonth = models.PositiveSmallIntegerField()
	idemp = models.PositiveSmallIntegerField()
	class Meta:
		verbose_name_plural = 'C110. Plan de Cuentas'
	def __str__(self):
		return self.nombre





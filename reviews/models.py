# -*- coding:utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Review(models.Model):
    user = models.ForeignKey(User)
    empresa = models.ForeignKey('Empresa')
    pros = models.CharField(max_length = 400)
    contras = models.CharField(max_length = 400)
    rating = models.IntegerField()


    def save(self, **kwargs):
        if self.rating > 5:
            raise ValidationError('Rating não pode ser maior que 5')
        if self.rating < 0:
            raise ValidationError('Rating não pode ser menor que 0')
        super(Review, self).save(**kwargs)

class Empresa(models.Model):
    nome = models.CharField(max_length = 50)

# -*- coding:utf8 -*-
from django.test import TestCase
from models import Review, Empresa
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class ReviewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.user.save()
        self.empresa = Empresa.objects.create()
        self.empresa.save()
        self.review = Review()
        self.review.user = self.user
        self.review.empresa = self.empresa

    def test_review_nao_deve_ter_rating_maior_que_5(self):
        review = self.review
        review.rating = 10
        try:
            review.save()
            self.fail('Rating não deve aceitar valores maiores que 5')
        except ValidationError:
            pass
        
    def test_review_nao_deve_ter_rating_menor_que_0(self):
        review = self.review
        review.rating = -1
        try:
            review.save()
            self.fail('Rating não deve aceitar valores menores que 0')
        except ValidationError:
            pass
        

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('nothing here. move along')

def adicionar(request):
    return HttpResponse('adicionando')

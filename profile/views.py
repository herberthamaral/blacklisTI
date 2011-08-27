from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blacklisTI.reviews.models import Review

@login_required
def index(request):
    reviews = Review.objects.filter(user = request.user)
    return render(request, 'profile/index.html', locals())

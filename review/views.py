# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import ReviewForm
from models import Review
from django.contrib.auth.decorators import login_required

def index(request):
    reviews = Review.objects.all()
    return render(request, 'review/index.html', locals())

@login_required
def adicionar(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(user = request.user)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('/review/')
            
    return render(request, 'review/adicionar.html', locals())

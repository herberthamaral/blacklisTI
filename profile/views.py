from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blacklisTI.review.models import Review

@login_required(login_url='/profile/login/')
def index(request):
    reviews = Review.objects.filter(user = request.user)
    return render(request, 'profile/index.html', locals())

def signup(request):
    form = auth.forms.UserCreationForm()
    if request.method == 'POST':
        form = auth.forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('/profile/')
    return render(request, 'profile/signup.html', locals())


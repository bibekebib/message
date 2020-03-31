from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return HttpResponse('Looks like your foform = AuthenticationForm(data= request.)rm have been saved!')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('user')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def userprofile(request):
    user = Profile.objects.all()
    return render(request, 'username.html', {'user': user})

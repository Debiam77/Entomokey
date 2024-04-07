from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from .forms import UserLoginForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Insect


def index(request):
    return render(request, 'entomokey/pages/index.html',{
        'user': request.user,
    })

def search(request):
    search_results = Insect.objects.all()
    
    if request.method == "POST":
        seach = request.POST.get('search_input', None)
        search_results = Insect.objects.filter(Q(username=search))
    else:
        return render(request, 'entomokey/pages/search.html', {
            'search_results': search_results,
        })



def entomokey_login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('entomokey:index')
        else:
            messages.error(request, "Erro no Login")
            return redirect('entomokey:user_login')
    else:    
        form = UserLoginForm()
        return render(request, 'entomokey/pages/auth.html', {
            'AUTH': 'login',
            'form': form,
            })


def entomokey_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                messages.error(request, "Senhas não são iguais!")
                return redirect(reverse('entomokey:register'))
            form.save()
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect(reverse('entomokey:index'))
        else:
            messages.error(request, form.errors)
            return redirect(reverse('entomokey:user_register'))
    else:
        form = UserCreationForm()

        return render(request, 'entomokey/pages/auth.html',{
            'AUTH': 'register',
            'form': form,
        })

def entomokey_logout(request):
    logout(request)
    return redirect('entomokey:index')

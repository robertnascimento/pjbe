from django.shortcuts import render, redirect
from .models import Carro,Moto,User
from .forms import UserForm, CarroForm , MotoForm

def bestcars(request):
    return render(request, 'bestcars.html')



def users(request):
    usr = User.objects.all()
    contexto = {
        'usuario': usr
    }
    return render(request, 'users.html', contexto)

def caduser(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('users')
        
    contexto = {
        'form_user': form
    }
    return render(request, 'caduser.html', contexto)



def carros(request):
    crr = Carro.objects.all()
    contexto = {
        'carro': crr
    }
    return render(request, 'carros.html', contexto)

def cadcar(request):
    formcar = CarroForm(request.POST or None)

    if formcar.is_valid():
        formcar.save()
        return redirect('carros')
        
    contexto = {
        'form_car': formcar
    }
    return render(request, 'cadcar.html', contexto)






def motos(request):
    motorcycle = Moto.objects.all()
    contexto = {
        'moto': motorcycle
    }
    return render(request, 'motos.html', contexto)

def cadmoto(request):
    fmoto = MotoForm(request.POST or None)

    if fmoto.is_valid():
        fmoto.save()
        return redirect('motos')
        
    contexto = {
        'form_moto': fmoto
    }
    return render(request, 'cadmoto.html', contexto)


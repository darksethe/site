from django.shortcuts import render, redirect
from django.http import HttpResponse
from .formulario import TreinaForm
from django.contrib import messages
from core.models import Treina_Facil, Assinar
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.


def Inicio(request):
    return render(request, 'index.html')


def Treinamento(request):
    return render(request, 'treinamento.html')

def login_user(request):
    return render(request,'login.html')

def Aulas(request):
    #treino = Treina_Facil.objects.all()
    form = TreinaForm()
    # if request.POST:
    #     form = TreinaForm(request.POST)
    # if form.is_valid():
    #     post = form.save(commit=False)
    #     post.save()
    # else:
    #     form = TreinaForm()
    return render(request, 'assinar.html', {'form': form})



def Treino(request):
    treino = Treina_Facil.objects.all()
    dados = {'tipo': treino}
    if treino.id == 6:
        print(f'o treino e {treino.Nome_do_treinamento}')
    return render(request, 'treinamento.html', dados)

@login_required(login_url='/login/')
def Lista_admin(request):
    assinar = Assinar.objects.all()
    busca= request.GET.get('search')
    if busca:
        assinar = Assinar.objects.filter(Cpf=busca)
    return render(request,'lista_admin.html',{'List':assinar})

def Pessoas(request):
    busca = request.GET.get('search')
    if busca:
        test = Assinar.objects.filter(Cpf_icontains=busca)
    return render(request, 'lista.html', {'assinar': test})

def submit_login(request):
    if request.POST:
        username = request.POST.get('uname')
        password= request.POST.get('pswd')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('lista/')
        else:
            messages.error(request,'usuario ou senha errado')
    return redirect('/')
@login_required(login_url='/login/')
def Lista(request):
    assinar = Assinar.objects.all()
    # dados = {'tipos': assinar}
    busca = request.GET.get('search')
    if busca:
        assinar = Assinar.objects.filter(Cpf=busca)
    return render(request, 'lista.html', {'List': assinar})

def delete(request,cpf):
    Assinar.objects.filter(Cpf=cpf).delete()
    return redirect('lista_admin/')

def Cadastrar(request):
    form = TreinaForm()
    if request.POST:
        form = TreinaForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('/')
    else:
        form = TreinaForm()

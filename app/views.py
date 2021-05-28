from django.shortcuts import render, redirect
from app.forms import *
import server

# Create your views here.
def homeScreen(request):
    data = {}
    data['form'] = ConsultaCepForm(request.POST)
    cliente = data['db'] = ConsultaCep.objects.all()
    if cliente:
        data['db'] = ConsultaCep.objects.all()[0]
    data['request'] = ''
    if data['form'].is_valid():
        data['form'].save()
        aux = data['form'].cleaned_data['cep']
        data['request'] = server.requisicao(aux)
    return render(request, 'index.html', data)

def create(request):
    form = ConsultaCepForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

def limpar(request, pk):
    pk = ConsultaCep.objects.get(pk=pk)
    pk.delete()
    return redirect('home')    

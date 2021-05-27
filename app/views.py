from django.shortcuts import render, redirect
from app.forms import  *
import requests
import server

# Create your views here.
def homeScreen(request):
    data = {}
    data['form'] = ConsultaCepForm(request.POST)
    data['db'] = ConsultaCep.objects.all()
    data['request'] = server.aux
    if data['form'].is_valid():
        data['form'].save()
    return render(request, 'index.html', data)
 


def create(request):
    form = ConsultaCepForm(request.POST)
    if form.is_valid():
        form.save()
        redirect('home')
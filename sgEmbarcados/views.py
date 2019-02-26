from django.shortcuts import render, redirect
from .form import *
import pprint
# Create your views here.


# Create your views here.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CRUD - Devices
def list_embedded(request):

    data = {}
    data['devices'] = Embedded.objects.all()
    return render(request, 'embarcados/list_embedded.html', data)


def new_embedded(request):

    data = {}
    form_embedded = FormEmbedded(request.POST or None)
    if 'btnSalvar' in request.POST:
        if form_embedded.is_valid():
            form_embedded.save()
            return redirect('list_embedded')
    elif 'btnCancelar' in request.POST:
        print('btnCancelar')
        return redirect('list_embedded')
    data['form_embedded'] = form_embedded
    data['btnSalvar'] = ''
    data['btnExcluir'] = 'disabled'
    data['btnCancelar'] = ''
    return render(request, 'embarcados/crud_embedded.html', data)


def update_embedded(request, pk):

    data = {}
    embedded = Embedded.objects.get(pk=pk)
    form_embedded = FormEmbedded(request.POST or None, instance=embedded)
    if 'btnCancelar' in request.POST:
        return redirect('list_embedded')
    elif 'btnExcluir' in request.POST:
        embedded.delete()
        return redirect('list_embedded')
    elif 'btnSalvar' in request.POST:
        if form_embedded.is_valid():
            form_embedded.save()
            return redirect('list_embedded')
    data['embedded'] = embedded
    data['form_embedded'] = form_embedded
    data['btnSalvar'] = 'disable'
    data['btnExcluir'] = 'disable'
    data['btnCancelar'] = 'disable'
    return render(request, 'embarcados/crud_embedded.html', data)


def delete_embedded(request,pk):

    embedded = Embedded.objects.get(pk=pk)
    embedded.delete()
    return redirect('list_embedded')
# -*- encoding: utf-8 -*-

# python import
import datetime

# django import
from django.http import HttpResponse
from django.template import RequestContext

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from main.forms import FormProposta
from main.models import Negocio

# Create your views here.
def teste (request):
    form = FormProposta()
    return render_to_response('teste.html', {'form': form, }, context_instance=RequestContext(request))


def home (request):
    # import pdb; pdb.set_trace()
    return render_to_response('index.html')

def novo_negocio (request):
    # import pdb; pdb.set_trace()
    if request.POST:
        form = FormProposta(request.POST)
        if form.is_valid():
            negocio = form.save(True)
            return redirect('/exibir_negocio/' + str(negocio.id) +'/')
        else:
            return redirect('/') # to do
    else:
        dct = {
            'form': FormProposta(),
        }

    return render_to_response('novo_negocio.html', dct, context_instance=RequestContext(request))

def listar_negocio (request):
    # import pdb; pdb.set_trace()
    dct = {
        'negocios': Negocio.objects.all(),
    }
    return render_to_response('listar_negocio.html', dct, context_instance=RequestContext(request))

def exibir_negocio (request, nid):
    # import pdb; pdb.set_trace()
    try:
        negocio = Negocio.objects.get(id=nid)
    except:
        return render_to_response('teste-404.html', {}, context_instance=RequestContext(request)) # TO DO: criar pagina de erro para negocio nao encontrado

    dct = {
        'negocio': negocio,
    }
    return render_to_response('exibir_negocio.html', dct, context_instance=RequestContext(request))

def editar_negocio (request, nid):
    # import pdb; pdb.set_trace()
    try:
        negocio = Negocio.objects.get(id=nid)
    except:
        return render_to_response('teste-404.html', {}, context_instance=RequestContext(request)) # TO DO: criar pagina de erro para negocio nao encontrado
    
    if request.POST:
        form = FormProposta(request.POST, instance=negocio)
        if form.is_valid():
            negocio=form.save(True)
            error = u'Alterações salvas com sucesso'
            return redirect('/exibir_negocio/' + str(negocio.id) + '/')
        else:
            error = form.errors
    else:
        form = FormProposta(instance=negocio)
        error = False
        
    dct = {
         'negocio': negocio,
         'action': '/editar_negocio/' + str(negocio.id) + '/',
         'form': form,
         'error': error,
         'submit_value': u'Atualizar',
    }
    return render_to_response('editar_negocio.html', dct, context_instance=RequestContext(request))

def excluir_negocio (request, nid):
    # import pdb; pdb.set_trace()
    try:
        negocio = Negocio.objects.get(id=nid)
    except:
        return render_to_response('teste-404.html', {}, context_instance=RequestContext(request)) # TO DO: criar pagina de erro para negocio nao encontrado

    negocio.delete()
    return redirect('/listar_negocio/')

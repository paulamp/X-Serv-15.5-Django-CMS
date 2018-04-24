from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages

# Create your views here.

def mostrar (request, identificador):
	try:
		pag = Pages.object.get(name= identificador)
		respuesta= "La pagina es " + valor.page
	except Pages.DoesNotExit:
		respuesta = "Pagina no existente"
	return HttpResponse (respuesta)
	
def listar (request):
	lista_paginas = Pages.objects.all()
	respuesta =" Las paginas son: </br>"
	for paginas in lista_paginas:
		respuesta +=  "Nombre del usuario: " + str(paginas.name) + "=>" + str(paginas.page) + " => " + "Identificador de la pagina" + str(paginas.id) + "</br>"
	return HttpResponse(str(respuesta))

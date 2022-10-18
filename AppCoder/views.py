from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.
def curso(request, nombre, camada):

    curso=Curso(nombre=nombre, camada=camada)
    curso.save()

    return  HttpResponse(f""" 
        <p> curso: {curso.nombre} - camada:{curso.camada} agregado </p>
    """)

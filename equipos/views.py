from django.shortcuts import render
from .models import Empleado
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def index(request):
    data = {"message": "Hello, world!"}
    return Response(data)

@api_view(['GET'])
def empleados(request):
    dataEmpleado = Empleado.objects.all()
    data= []
    for d in dataEmpleado:
        data.append({
            'nombre': d.nombre,
            'email' : d.email,
            'cargo' : d.cargo
        })
    return Response(data)

@api_view(['POST'])
def crearEmpleado(request):
    nombre = request.data['nombre']
    email = request.data['email']
    cargo = request.data['cargo']

    nuevoEmpleado = Empleado.objects.create(nombre=nombre, email=email, cargo=cargo)
    data= {
        'respuesta' : 'OK'
    }
    
    return Response(data)
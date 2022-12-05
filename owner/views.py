from django.shortcuts import render

# Create your views here.
from owner.models import Owner


def owner_list(request):
    data_context = {
        'nombre_owner': 'Katty Paredes',
        'edad': 24,
        'pais': 'Perú',
        'dni': '12345678',
        'vigente': True
    }

    owners = [
        {
            'nombre_owner': 'Daniel Ordenado',
            'edad': 20,
            'pais': 'Perú',
            'dni': '12345678',
            'vigente': True
        },
        {
            'nombre_owner': 'Katty Paredes',
            'edad': 24,
            'pais': 'Brasil',
            'dni': '43340690',
            'vigente': True
        },
        {
            'nombre_owner': 'Carlos Carbajal',
            'edad': 28,
            'pais': 'Perú',
            'dni': '42305699',
            'vigente': True
        },
        {
            'nombre_owner': 'Juan Ríos',
            'edad': 34,
            'pais': 'México',
            'dni': '11395600',
            'vigente': True
        }
    ]


    """Crear un objeto en la Base de Datos para la tabla de owner"""
    p = Owner(nombre="Rossmery",pais="España", edad=21)
    p.save() # Guarda el registro en la B.D.

    p.nombre = "Beatriz"
    p.save()

    return render(request, 'owner/owner_list.html', context={'data': owners})

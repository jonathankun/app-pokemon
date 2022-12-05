from django.shortcuts import render

# Create your views here.
from owner.models import Owner
from django.db.models import F
from django.db.models import Q

def owner_list(request):
    data_context = {
        'nombre_owner': 'Katty Paredes',
        'edad': 24,
        'pais': 'Perú',
        'dni': '12345678',
        'vigente': True
    }

    # owners = [
    #     {
    #         'nombre_owner': 'Daniel Ordenado',
    #         'edad': 20,
    #         'pais': 'Perú',
    #         'dni': '12345678',
    #         'vigente': True
    #     },
    #     {
    #         'nombre_owner': 'Katty Paredes',
    #         'edad': 24,
    #         'pais': 'Brasil',
    #         'dni': '43340690',
    #         'vigente': True
    #     },
    #     {
    #         'nombre_owner': 'Carlos Carbajal',
    #         'edad': 28,
    #         'pais': 'Perú',
    #         'dni': '42305699',
    #         'vigente': True
    #     },
    #     {
    #         'nombre_owner': 'Juan Ríos',
    #         'edad': 34,
    #         'pais': 'México',
    #         'dni': '11395600',
    #         'vigente': True
    #     }
    # ]


    """Crear un objeto en la Base de Datos para la tabla de owner"""
    # p = Owner(nombre="Rossmery",pais="España", edad=21)
    # p.save() # Guarda el registro en la B.D.
    #
    # p.nombre = "Beatriz"
    # p.save()

    """Obtener todos los elementos de una tabla en la BD"""

    owners = Owner.objects.all()

    """Filtración de datos: filter()"""
    #owners = Owner.objects.filter(nombre="Omar")

    """Filtración de datos con AND y SQL: filter()"""
    #owners = Owner.objects.filter(nombre="Rossmery", edad=28)

    """Filtración de Datos más precisos con:__contains"""
    #owners = Owner.objects.filter(nombre__contains="Rossmery")

    """Filtración de datos más precisos con: __endwith()"""
    #owners = Owner.objects.filter(nombre__endswith="go")

    """Obtener un solo dato u objeto de la tabla"""
    #owners = Owner.objects.get(dni="56238932")
    #owners = Owner.objects.get(nombre="Rossmery")
    #print("El dato es: {}".format(owners))
    #print("Tipo de dato: {}".type(owners))

    """Ordenar por cualquier atributo o campo en la Base de Datos"""

    """Ordenar alfabeticamente """
    #owners = Owner.objects.order_by('-edad')

    """Ordenar concatenando diferentes métodos de ORM"""
    #owners = Owner.objects.filter(nombre="Rossmery").order_by("-edad")

    """Acortar datos: Obtener un rango de registro de la tabla en la B.D."""
    #owners = Owner.objects.all()[2:6]

    """Eliminando un conjunto de datos especificos"""
    #p = Owner.objects.filter(id=2)
    #p.delete() #Eliminamos el registro que encontró

    """Actualización de datos en la BD a un cierto grupo de datos"""

    #Owner.objects.filter(pais__startswith="Esp").update(edad=36)

    """Utilizando  F expresiones"""
    #Owner.objects.filter(edad__gte=30).update(edad=F('edad') -15)

    """Consultas complejas"""
    #query = Q(pais__startswith ='Pe') | Q(pais__startswith='Br')
    #owners = Owner.objects.filter(query)

    """Negar Q"""
    #query = Q(pais__startswith ='Pe') & ~Q(edad=21)
    #owners = Owner.objects.filter(query)

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')
    owners = Owner.objects.filter(query, edad=21)

    """Error de consulta Q, no es válido"""
    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')
    #owners = Owner.objects.filter(edad=21, query)

    return render(request, 'owner/owner_list.html', context={'data': owners})

def owner_search(request):
    query = request.GET.get('q', '')

    result = (
        Q(nombre__icontains=query)
    )

    datacontext = Owner.objects.filter(result).distinct()

    return render(request, 'owner/owner_seach.html', context={'data': datacontext, 'query': query})

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from owner.forms import OwnerForm
from owner.models import Owner
from django.db.models import F, Q

from django.views.generic import ListView, DeleteView, CreateView, UpdateView

#Serialize
from django.core import serializers as ssr

#DRF
from owner.serializers import OwnerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')
    #owners = Owner.objects.filter(query, edad=21)

    """Error de consulta Q, no es válido"""
    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')
    #owners = Owner.objects.filter(edad=21, query)

    return render(request, 'owner/owner_list.html', context={'data': owners})

def owner_search(request):
    query = request.GET.get('q', '')

    # icontains: busca lo que escribimos en el buscador
    print("Query: {}".format(query))
    result = (
         Q(nombre__icontains=query)
    )
    datacontext = Owner.objects.filter(result).distinct()

    return render(request, 'owner/owner_seach.html', context={'data': datacontext, 'query': query})

def owner_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    owners = Owner.objects.all()
    #print("El tipo de dato de la variable es: {}".format(type(owners)))
    #print(owners)
    return render(request, 'owner/owners_details.html', context={'data': owners})

def owner_create(request):

     if request.method == "POST":
         print("ES UN POST")
         form = OwnerForm(request.POST)
         if form.is_valid():
             #nombre = form.cleaned_data['nombre']
             #print("Nombre: {}".format(nombre))
             #edad = form.cleaned_data['edad']
             #pais = form.cleaned_data['pais']
             try:
                 form.save()
                 return redirect('owner_list')
             except:
                 pass
     else:
         form = OwnerForm()
     return render(request, 'owner/owner-create.html', {'form': form})

def owner_delete(request, id_owner):
    print("ID: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()
    return redirect('owner_detail')

def owner_edit(request, id_owner):
     owner = Owner.objects.get(id=id_owner)
     form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

     if request.method == 'POST':
         form = OwnerForm(request.POST, instance=owner)
         if form.is_valid():
             form.save()
             return redirect('owner_detail')

     return render(request, 'owner/owner_update.html', {'form': form})

def owner_list_ref03_01(request):
    owners = Owner.objects.all()
    dataperu = Owner.objects.filter(pais="Perú")
    dataargentina = Owner.objects.filter(pais="Argentina")

    return render(request, 'owner/owner_list_ref03_01.html', context={'data': owners, 'dataperu': dataperu, 'dataargentina': dataargentina})

def owner_search_ref03_02(request):
    query = request.GET.get('q', '')

    # icontains: busca lo que escribimos en el buscador
    print("Query: {}".format(query))
    result = (
         Q(nombre__icontains=query)
    )
    datacontext = Owner.objects.filter(result).distinct()

    return render(request, 'owner/owner_search_ref03_02.html', context={'data': datacontext, 'query': query})


def owner_edit_ref03_01(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list_ref03_01')

    return render(request, 'owner/owner_update_ref03_01.html', {'form': form})

def owner_delete_ref03_01(request, id_owner):
    print("ID: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        owner.delete()
        return redirect('owner_list_ref03_01')

    return render(request,'owner/owner-confirm-delete-ref03_01.html', {'form': form})

"""Vistas basadas en clases"""
"""ListView, CreateView, UpdateView, DeleteView"""

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_vc.html'

class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner-create.html'
    success_url = reverse_lazy('owner_list_vc')

class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    success_url = reverse_lazy('owner_list_vc')
    template_name = 'owner/owner_update-vc.html'

class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc') #Lazy cuando ha sido exitoso
    template_name = 'owner/owner-confirm-delete.html'

class OwnerList_ref03(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc_ref03.html'

class OwnerCreate_ref03(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create_vc_ref03.html'
    success_url = reverse_lazy('owner_list_vc_ref03')

class OwnerUpdate_ref03(UpdateView):
    model = Owner
    form_class = OwnerForm
    success_url = reverse_lazy('owner_list_vc_ref03')
    template_name = 'owner/owner_update_vc_ref03.html'

class OwnerDelete_ref03(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc_ref03') #Lazy cuando ha sido exitoso
    template_name = 'owner/owner-confirm-delete.html'

"""Serializers"""
def ListOwnerSerializer(request):
    lista = ssr.serialize('json', Owner.objects.all(), fields=['nombre', 'pais', 'edad'])
    return HttpResponse(lista, content_type="application/json")

"""Vistas creadas con Django Rest Framework"""

@api_view(['GET', 'POST'])
def owner_api_view(request):
    if request.method =='GET':
        queryset = Owner.objects.all() #Se obtiene los datos de la tabla owner
        serializers_class = OwnerSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)

    elif request.method =='POST':
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def owner_detail_view(request, pk):
    owner = Owner.objects.filter(id=pk).first()

    if owner:
        if request.method == 'GET':
            serializers_class = OwnerSerializer(owner)
            return Response(serializers_class.data)

        elif request.method == 'PUT':
            serializers_class = OwnerSerializer(owner, data=request.data)

            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            owner.delete()
            return Response('Owner se ha eliminado correctamente', status=status.HTTP_201_CREATED)

    return Response({'message': 'No se ha encontrado ningun owner con estos datos'}, status= status.HTTP_400_BAD_REQUEST)



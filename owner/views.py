from django.shortcuts import render

# Create your views here.


def owner_list(request):
    data_context = {
        'nombre_owner': 'Kevin Melgarejo',
        'edad': 18,
        'pais': 'Perú',
        'vigente': True
    }

    return render(request, 'owner_list.html', context={'data': data_context})

from django.contrib import admin
from .models import Owner

# Register your models here.
#admin.site.register(Owner)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais','edad') #Configura datos a visualizar en a lista de registros admin
    search_fields = ('nombre', 'pais')  #Agrega un campo de busqueda en la parte adminbistrativa
    fields = ('nombre', 'edad') #Oculta o visualiza los campos  campos al momento de crear


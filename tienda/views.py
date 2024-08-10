from django.shortcuts import render
from .models import Producto 




# Create your views here.
#--- import la clase hacia la vista tienda.html APP
def tienda(request):
    productos=Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})


 
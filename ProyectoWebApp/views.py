

from django.shortcuts import render, HttpResponse
#from servicios.models import Servicio
from carro.carro import Carro

# la primera referencia 'servicios' hace referencia a la app
# "Carro" hace  referencia a la clase carro para que inicie antes de cargar la app

#from carro.carro import Carro



# Create your views here.
def home(request):
    carro=Carro(request)
    return render(request, 'ProyectoWebApp/home.html')


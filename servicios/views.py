from django.shortcuts import render

from servicios.models import Servicio
from django.contrib.auth.decorators import login_required

# Create your views here.
#---- SERVICIOS APP
@login_required
def servicios(request):
   servicios = Servicio.objects.all()
   return render(request, 'servicios/servicios.html', {'servicios': servicios})

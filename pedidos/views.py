from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedidos, LineaPedido
from carro.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Producto
 
# Create your views here.
@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedidos.objects.create(user=request.user)# damos de alta un pedido
    carro=Carro(request) # cogemos el carro
    lineas_pedido=list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items():  #recorremos el carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)  # crea registros en BBDD en paquete
    enviar_email(  #enviamos mail al cliente
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )

#mensaje para el futuro
    messages.success(request, "EL pedido hecho correctamente")
    return redirect("../tienda")
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})

def enviar_email(**kwargs):
    asunto="gracias por el pedido"
    mensaje=render_to_string("email/pedidos.html",{
          "pedido": kwargs.get("pedido"),
          "lineas_pedido": kwargs.get("lineas_pedido"),
          "nombre_usuario": kwargs.get("nombre_usuario")
     })

    mensaje_texto=strip_tags(mensaje)
    from_email="curso@gmail.com"
    #to=kwargs.get("email_usuario")
    to="correo@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
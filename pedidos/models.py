from django.db import models
from tabnanny import verbose

from django.contrib.auth import get_user_model #devuelve el usuario activo actual
from tienda.models import Producto 
from django.db.models import F,Sum, FloatField  # para calcular el total de una orden de pedido


# Create your models here.
User=get_user_model()

class Pedidos(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)# Cuando se elimine un usuario sus pedidos se eliminirán en cascada
    created_at=models.DateTimeField(auto_now_add=True) #Para le fecha de pedido automática


    @property
    def total(self):
        return self.lineapedido_set.aggregate(
        total=Sum(F('precio')*F('cantidad'), output_field=FloatField())
        )['total'] or FloatField(0)


    def __str__(self):
        return self.id


class Meta:
    db_table='pedidos'
    verbose_name='pedido'
    verbose_name_plural='pedidos'
    ordering=['id']


class LineaPedido(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'


 
class Meta:  
    db_table='lineapedidos'
    verbose_name=' Liena Pedido' 
    verbose_name_plural='Lineas Pedidos'
    ordering=['id']
from django.urls import path
from .import views
#from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.blog, name='Blog'),
    #--- " INT " convierte el string en entero
    path('categoria/<int:categoria_id>/', views.categoria, name='Categoria'),

]


#urlpatterns += static(
    #settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    #)
 
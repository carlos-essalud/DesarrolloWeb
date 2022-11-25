from django.urls import path
from django.urls import path

from ProjectoWebApp import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('servicios',views.servicio, name="Servicios"),
    path('tienda',views.tienda, name="Tienda"),
    path('blog',views.blog, name="Blog"),
    path('contacto',views.contacto, name="Contacto"),
]
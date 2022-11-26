from django.shortcuts import render,HttpResponse

from servicios.models import Servicio

# Create your views here.

def home(request):
    return render(request,"ProjectoWebApp/home.html")

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request,"ProjectoWebApp/servicio.html", {'servicios': servicios})
 
def tienda(request):
    return render(request,"ProjectoWebApp/tienda.html")

def blog(request):
    return render(request,"ProjectoWebApp/blog.html")

def contacto(request):
    return render(request,"ProjectoWebApp/contacto.html")
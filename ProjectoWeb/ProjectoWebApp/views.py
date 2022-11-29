from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"ProjectoWebApp/home.html")
 
def tienda(request):
    return render(request,"ProjectoWebApp/tienda.html")

def contacto(request):
    return render(request,"ProjectoWebApp/contacto.html")
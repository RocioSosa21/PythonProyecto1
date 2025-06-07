from django.shortcuts import render

def index(request):
    context = {"mensaje": "Bievenidos a mi aplicacion Django"}
    return render(request,"miapp/index.html",context)

# Create your views here.

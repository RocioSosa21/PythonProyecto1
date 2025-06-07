from django.http import HttpResponse
from django.shortcuts import render 

# def saludo(request):
#     return HttpResponse("Hola Django - Code") # Crea una funcion de vista: define de manera logica la vista

def saludo(request): 
    contexto = {'mensaje': 'Hola Django - Coder'} 
    return render(request, 'miapp/saludo.html', contexto)
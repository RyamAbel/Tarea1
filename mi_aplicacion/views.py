from django.shortcuts import render

# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para la página "Acerca de"
def acerca(request):
    return render(request, 'acerca.html')


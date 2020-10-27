from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Persona, Profesion, Distrito

# Create your views here.

class index(ListView):
    model = Persona
    template_name = 'index.html'
    paginate_by = 3

def searchProfesional(request):
    template_name = "searchProfesional.html"
    input = request.GET['textSearch']
    profesionales = Persona.objects.filter(profesion__nombre__icontains=input)
    context = {
        'listaProfesionales': profesionales
    }
    return render(request, template_name, context)

def detailProfesional(request, id):
    template_name = 'detail.html'
    profesional = Persona.objects.get(id=id)
    context = {
        'profesional': profesional
    }
    return render(request, template_name, context)





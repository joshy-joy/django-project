from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

def home(request):

    Pets = Pet.objects.all()
    return render(request, 'home.html', {'Pets':Pets})

def pet_details(request, id):

    try:
        pet = Pet.objects.get(id = id)

    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')

    return render(request, 'pet_details.html', {'pet':pet})

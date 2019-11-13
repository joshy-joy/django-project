from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'home.html')

def order(request):

    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering. Your %s pizza with %s and %s is on the Way!'%(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            new_form = PizzaForm() 
            return render(request, 'order.html', {'pizzaform':new_form,'note':note})
    else:
        pizzaform = PizzaForm()
        return render(request, 'order.html', {'pizzaform':pizzaform})

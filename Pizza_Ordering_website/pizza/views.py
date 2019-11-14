from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza


def home(request):
    return render(request, 'home.html')

def order(request):

    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():

            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thanks for ordering. Your %s pizza with %s and %s is on the Way!'%(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            new_form = PizzaForm() 
            return render(request, 'order.html', {'pizzaform':new_form,'note':note, 'multiple_form' : multiple_form, 'id': created_pizza_pk})
    else:
        pizzaform = PizzaForm()
        return render(request, 'order.html', {'pizzaform':pizzaform, 'multiple_form' : multiple_form})

def pizzas(request):

    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)

    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra = number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)

        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['toppin1'])
            note = 'Pizza has Been Ordered'

        else:
            note = 'Order Was not created'
        return render(request, 'pizzas.html', {'note': note, 'formset': formset})

    else:
        return render(request, 'pizzas.html', {'formset': formset})

def edit_order(request, pk):

    pizza = Pizza.objects.get(id = pk)
    form = PizzaForm(instance = pizza)

    if request == 'POST':
        filled_form = PizzaForm(request.POST, instance = pizza)

        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order Successfully updated'
        return render(request, 'edit_order.html', {'note': note, 'pizzaform': form, 'pizza': pizza})

    return render(request, 'edit_order.html', {'pizzaform': form, 'pizza': pizza})


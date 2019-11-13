from django import forms

class PizzaForm(forms.Form):

    SIZE = [('Small', 'Small'),('Medium', 'Medium'), ('Large', 'Large')]
    topping1 = forms.CharField(label = "topping1", max_length = "100")
    topping2 = forms.CharField(label = "topping2", max_length = "100")
    size = forms.ChoiceField(label = "Size", choices = SIZE)
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'vote/pizza_list.html', {'pizzas': pizzas})

def vote(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == 'POST':
        pizza.votes += 1
        pizza.save()
    return redirect('pizza_list')

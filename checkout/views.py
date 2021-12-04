from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messaes.error(request, "There's nothing in your bag the moment")
        return redirect(reverse('prod'))


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51K2yXaJPAQhAIeGis7WdMHP3hzInDuO9Mvjt1KRadolFsTRKWxrsYABWuGJCCrpJFWv6haLcTX4E5zenPg6rWMiu00qTFSLAPe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


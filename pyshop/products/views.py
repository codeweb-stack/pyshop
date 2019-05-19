from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from .models import Offer


# Create your views here.
# /products -> index

def index(request):
    products = Product.objects.all()
    offers = Offer.objects.all()
    return render(request, 'index.html',
                  {'products': products, 'offers': offers})


def new(request):
    return HttpResponse('new Products')

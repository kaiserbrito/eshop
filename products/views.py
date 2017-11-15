from django.shortcuts import render
from django.views.generic import View
from .models import Product

# Create your views here.

class Home(View):
  def get(self, request, *args):
    return render (request, 'home.html')

def product_list(request):
  products = Product.objects.all()
  return render(request, 'products/product_list.html', {'products': products})

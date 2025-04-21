from django.http import Http404
from django.shortcuts import render

from product.models import Product





def product_list(request):
    products = Product.objects.all()
    template_name = 'List.html'
    return render(request, template_name, {"products": products})

def product_details(request, product_id):
    try:
        product = Product.objects.get(id = product_id)

        template_name = "details.html"
        return render(request, template_name, {"product": product})
    except Product.DoesNotExist:
        raise Http404("Товар не найден")
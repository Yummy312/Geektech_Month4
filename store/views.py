from django.shortcuts import HttpResponse, render
import datetime
from store.models import Product, Review
# Create your views here.


def greet(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(f"Now: {datetime.datetime.now()}")


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")


def main_view(request):
    if request.method == 'GET':
        return render(request, 'templates/layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product)

        context = {
            'product': product,
            'reviews': reviews
        }

        return render(request, 'products/detail.html', context=context)

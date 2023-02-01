from django.shortcuts import HttpResponse, render, redirect
import datetime
from store.models import Product, Review, Category
from store.forms import ProductCreateForm, ReviewCreateForm


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
            'products':products,
            'user': request.user
        }
        print(request.user)
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product)
        context = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product)
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                author_id=request.user.id,
                text=form.cleaned_data.get('text'),
                product=product
            )
            return redirect(f'/products/{product.id}/')

        return render(request, 'products/detail.html', context={
            'product': product,
            'reviews': reviews,
            'form': form,
            'user': request.user
        })


def show_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request,'categories/index.html', context=context)


def detail_categories(request, category_id):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        category_products = Product.objects.filter(category=category)
        context = {
            'category_products': category_products
        }
        return render(request, 'categories/category_detail.html', context=context)


def create_products_view(request):
    if request.method == "GET" and not request.user.is_anonymous: # Проверка на пользователя
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/products/')

    if request.method == 'POST' or 'post':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description = form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 10
            )
            return redirect('/products/')

        """Если данные не прошли валидацию"""
        return render(request, 'products/create.html', context={'form': form})


""" Кастомная валидация """

# def create_form_products(request):
#     if request.method == "GET":
#         return render(request, 'products/create.html')
#     if request.method == 'POST' or 'post':
#         data = request.POST
#         """data validation"""
#         errors = {}
#
#         if len(data['text'])< 5:
#             errors['text']='Min length 5'
#         """if all OK"""
#         if errors.keys().__len__()<1:
#             Review.objects.create(
#                 text=data.get('text')
#             )
#             return redirect('/products/')
#         return render(request, 'products/create.html', context={'errors': errors})




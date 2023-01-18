from django.shortcuts import HttpResponse, render
import datetime
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


def show_products(request):
    if request.method == 'GET':
        return render(request, 'templates/layouts/index.html')



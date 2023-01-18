from django.urls import path
from store.views import greet, goodbye, now_date, show_products

urlpatterns = [
    path('hello/', greet),
    path('now_date/', now_date),
    path('goodby/', goodbye),
    path('', show_products)
]

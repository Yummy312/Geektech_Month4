from django.urls import path
from store.views import greet, goodbye, now_date, main_view, products_view,  product_detail_view

urlpatterns = [
    path('hello/', greet),
    path('now_date/', now_date),
    path('goodby/', goodbye),
    path('', main_view),
    path('products/', products_view ),
    path('products/<int:product_id>/', product_detail_view)
]

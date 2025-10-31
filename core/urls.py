from django.urls import path

from .views import *

urlpatterns = [
    path('', main),
    path('buy', buy),
    path('myname', name),
    path('products', products),
    path('filials', filials),
    path('products/<int:product_id>',  product_detail, name='product_detail'),
    path('products/add', add_product, name='add_product'),
    path('filials/add', add_filial),
    path('categories/<int:category_id>', products_category),
    path('feedback', feedback, name='feedback')
]
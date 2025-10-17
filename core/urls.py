from django.urls import path

from .views import *

urlpatterns = [
    path('', main),
    path('buy', buy),
    path('myname', name),
    path('products', products),
    path('filials', filials)
]
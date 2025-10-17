from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def main(request):
    return render(request, 'main.html')


def buy(request):
    return HttpResponse('Пока!')


def name(request):
    myname = 'Илья Евдокимов 2'

    context = {'name_template': myname}
    return render(request, 'name.html', context)


def products(request):
    products_list = [
        {'name': 'Молоко', 'price': 50, 'discount': True},
        {'name': 'Хлеб', 'price': 100, 'discount': False}
    ]
    # получить товары из базы
    products_list_db = Product.objects.all()

    context = {'products_list': products_list_db}
    return render(request, 'products.html', context)

def filials(request):
    filials_list = [
        {'address': 'Ленина 1 ', 'name': 'Первый'},
        {'address': 'Пушкина 2', 'name': 'Очень большой'}
    ]

    context = {'filials_list': filials_list}
    return render(request, 'filials.html', context)
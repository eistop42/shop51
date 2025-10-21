from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Filial

def main(request):
    return render(request, 'main.html')


def buy(request):
    return HttpResponse('Пока!')


def name(request):
    myname = 'Илья Евдокимов 2'

    context = {'name_template': myname}
    return render(request, 'name.html', context)


def products(request):

    # получить товары из базы
    products_list_db = Product.objects.all()

    context = {'products_list': products_list_db}
    return render(request, 'products.html', context)


def product_detail(request, product_id):

    # достали товар из базы
    product = Product.objects.get(id=product_id)

    context = {'product_template': product}

    return render(request, 'product_detail.html', context)

def filials(request):

    filials_list = Filial.objects.all()

    context = {'filials_list': filials_list}
    return render(request, 'filials.html', context)
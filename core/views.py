from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product, Filial, ProductCategory

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
    categories = ProductCategory.objects.all() # select * from Product_category

    context = {'categories': categories}
    return render(request, 'products.html', context)


def products_category(request, category_id):

    category = ProductCategory.objects.get(id=category_id)

    # получаем все товары из категории
    products = Product.objects.filter(category_id=category_id)

    context = {'category': category, 'products': products}
    return render(request, 'products_category.html', context)


def product_detail(request, product_id):

    # достали товар из базы
    product = Product.objects.get(id=product_id)

    context = {'product_template': product}

    return render(request, 'product_detail.html', context)

def filials(request):

    filials_list = Filial.objects.all()

    context = {'filials_list': filials_list}
    return render(request, 'filials.html', context)


def add_product(request):

    errors = ''
    title = ''

    # обработка формы
    if request.method == 'POST':
        # 1. Достать данные из запроса
        title = request.POST.get('title')
        count = request.POST.get('count')
        price = request.POST.get('price')
        category = request.POST.get('category')

        # проверить существование категории
        if ProductCategory.objects.filter(id=category).exists():
            category = ProductCategory.objects.get(id=category)
        else:
            category = None

        # 2 Проверить на валидность
        if title and count and price and category:
        # 3. Если все ок - создать новый объект в базе.

            Product.objects.create(name=title, count=count, price=price, category=category)
            # 4. Куда-то перенаправить пользователя
            return redirect('/products')
        else:
            errors = 'Не заполнены некотрые поля'

    categories = ProductCategory.objects.all() # select * from core_product_category

    context = {'errors': errors, 'title': title, 'categories': categories}

    return render(request, 'add_product.html', context)


def add_filial(request):

    errors = ''
    if request.method == 'POST':
        #1. Достать поля
        #2. Если все есть - добавить объект в базу
        name = request.POST.get('name')
        address = request.POST.get('address')
        rating = request.POST.get('rating')
        description = request.POST.get('description')

        if name and address and rating and description:
            Filial.objects.create(name=name, address=address, rating=rating,
                                  text=description)
            return redirect('/filials')

    return render(request, 'add_filial.html')


def feedback(request):

    return render(request, 'feedback.html')
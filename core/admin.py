from django.contrib import admin

from .models import Product, Filial, ProductCategory, Feedback

admin.site.register(Product)
admin.site.register(Filial)
admin.site.register(ProductCategory)
admin.site.register(Feedback)


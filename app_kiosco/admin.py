from django.contrib import admin
from .models import Supplier, Product, Purchase, Sale

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Sale)

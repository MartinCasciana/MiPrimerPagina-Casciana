from django.db.models import Sum, F, Value
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Purchase, Sale
from itertools import chain

import csv

from .models import Product, Supplier, Movement
from .forms import SupplierForm, ProductForm, PurchaseForm, SaleForm, SearchForm

def home(request):
    return render(request, "app_kiosco/home.html")

class ProductListView(ListView):
    model = Product
    template_name = 'app_kiosco/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        qs = Product.objects.all()
        qs = qs.annotate(
            purchased=Coalesce(Sum('purchases__qty'), Value(0)),
            sold=Coalesce(Sum('sales__qty'), Value(0)),
        ).annotate(stock=F('purchased') - F('sold'))
        return qs

def product_search(request):
    form = SearchForm(request.GET or None)
    products = Product.objects.none()
    if form.is_valid():
        qs = Product.objects.all()
        if form.cleaned_data.get('q'):
            qs = qs.filter(name__icontains=form.cleaned_data['q'])
        if form.cleaned_data.get('barcode'):
            qs = qs.filter(barcode__icontains=form.cleaned_data['barcode'])
        if form.cleaned_data.get('category'):
            qs = qs.filter(category__icontains=form.cleaned_data['category'])
        products = qs.annotate(
            purchased=Coalesce(Sum('purchases__qty'), Value(0)),
            sold=Coalesce(Sum('sales__qty'), Value(0)),
        ).annotate(stock=F('purchased') - F('sold'))
    return render(request, "app_kiosco/search.html", {"form": form, "products": products})

def supplier_create(request):
    form = SupplierForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "app_kiosco/supplier_form.html", {"form": form})

def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "app_kiosco/product_form.html", {"form": form})

def purchase_create(request):
    form = PurchaseForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        purchase = form.save()
        Movement.objects.create(
            product=purchase.product, type='IN',
            qty=purchase.qty, unit_amount=purchase.unit_cost, date=purchase.date
        )
        messages.success(request, "Compra registrada.")
        return redirect("product_list")
    return render(request, "app_kiosco/purchase_form.html", {"form": form})

def sale_create(request):
    form = SaleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        sale = form.save()
        Movement.objects.create(
            product=sale.product, type='OUT',
            qty=sale.qty, unit_amount=sale.unit_price, date=sale.date
        )
        messages.success(request, "Venta registrada.")
        return redirect("product_list")
    return render(request, "app_kiosco/sale_form.html", {"form": form})

def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto actualizado.")
        return redirect("product_list")
    return render(request, "app_kiosco/product_form.html", {"form": form})

def supplier_update(request, pk):
    obj = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proveedor actualizado.")
        return redirect("product_list")
    return render(request, "app_kiosco/supplier_form.html", {"form": form})

def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        name = str(obj)
        obj.delete()
        messages.success(request, f"Producto '{name}' borrado.")
        return redirect("product_list")
    return render(request, "app_kiosco/confirm_delete.html", {"object": obj, "type": "Producto"})

def supplier_delete(request, pk):
    obj = get_object_or_404(Supplier, pk=pk)
    if obj.product_set.exists():
        messages.error(request, "No se puede borrar: el proveedor tiene productos asociados.")
        return redirect("product_list")
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Proveedor borrado.")
        return redirect("product_list")
    return render(request, "app_kiosco/confirm_delete.html", {"object": obj, "type":"Proveedor"})

def movement_history(request):
    qs = Movement.objects.select_related('product').all()
    product = request.GET.get('product','').strip()
    if product:
        qs = qs.filter(product__name__icontains=product)
    return render(request, "app_kiosco/movement_history.html", {"movements": qs})

def export_products_csv(request):
    qs = Product.objects.all().values_list('name', 'barcode', 'category', 'sale_price')
    resp = HttpResponse(content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename="productos.csv"'
    writer = csv.writer(resp)
    writer.writerow(['Nombre', 'Código', 'Categoría', 'Precio venta'])
    for row in qs:
        writer.writerow(row)
    return resp

def history(request):
    purchases = Purchase.objects.select_related("product").all()
    sales = Sale.objects.select_related("product").all()

    entries = []
    for c in purchases:
        entries.append({
            "date": c.date,
            "type": "Compra",
            "product": c.product,
            "qty": c.qty,
            "unit_amount": c.unit_cost,
        })
    for v in sales:
        entries.append({
            "date": v.date,
            "type": "Venta",
            "product": v.product,
            "qty": v.qty,
            "unit_amount": v.unit_price,
        })

    entries.sort(key=lambda e: e["date"], reverse=True)

    q = (request.GET.get("q") or "").strip()
    if q:
        entries = [e for e in entries if q.lower() in str(e["product"]).lower()]

    return render(request, "app_kiosco/history.html", {"entries": entries, "q": q})
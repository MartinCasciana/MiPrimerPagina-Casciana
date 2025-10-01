from django import forms
from .models import Supplier, Product, Purchase, Sale
from django.db.models import Sum

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "phone", "email"]
        labels = {
            'name': 'Nombre',
            'phone': 'Teléfono',
            'email': 'Correo Electrónico',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "barcode", "category", "supplier", "cost_price", "sale_price"]
        labels = {
            "name": "Nombre",
            "barcode": "Código de barras",
            "category": "Categoría",
            "supplier": "Proveedor",
            "cost_price": "Precio de costo",
            "sale_price": "Precio de venta",
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["product", "qty", "unit_cost", "date"]
        labels = {
            "product": "Producto",
            "qty": "Cantidad",
            "unit_cost": "Costo unitario",
            "date": "Fecha",
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["product", "qty", "unit_price", "date"]
        labels = {
            "product": "Producto",
            "qty": "Cantidad",
            "unit_price": "Precio unitario",
            "date": "Fecha",
        }

    def clean(self):
        cleaned = super().clean()
        product = cleaned.get("product")
        qty = cleaned.get("qty") or 0
        if product:
            purchased = product.purchases.aggregate(total=Sum('qty'))['total'] or 0
            sold = product.sales.aggregate(total=Sum('qty'))['total'] or 0
            stock = purchased - sold
            if qty > stock:
                raise forms.ValidationError(f"No hay stock suficiente. Disponible: {stock}.")
        return cleaned

class SearchForm(forms.Form):
    q = forms.CharField(label="Nombre contiene", required=False)
    barcode = forms.CharField(label="Código de barras", required=False)
    category = forms.CharField(label="Categoría", required=False)

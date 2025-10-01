from django.db import models
from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    barcode = models.CharField(max_length=50, blank=True, null=True, unique=True)
    category = models.CharField(max_length=80, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="purchases")
    qty = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Compra {self.product.name} x{self.qty}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    qty = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Venta {self.product.name} x{self.qty}"

class Movement(models.Model):
    MOVEMENT_TYPES = (('IN','Compra'), ('OUT','Venta'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    qty = models.PositiveIntegerField()
    unit_amount = models.DecimalField(max_digits=10, decimal_places=2)  # costo o precio
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'

    def __str__(self):
        return f"{self.get_type_display()} {self.product} x{self.qty}"
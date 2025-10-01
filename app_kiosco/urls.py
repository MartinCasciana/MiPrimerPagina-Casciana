from django.urls import path
from .views import (
    home, ProductListView, product_search,
    supplier_create, product_create, purchase_create, sale_create, product_update, product_delete,
    supplier_update, supplier_delete, movement_history, export_products_csv, history
)

urlpatterns = [
    path('', home, name='home'),
    path('buscar/', product_search, name='product_search'),
    path('productos/', ProductListView.as_view(), name='product_list'),
    path('proveedores/nuevo/', supplier_create, name='supplier_create'),
    path('productos/nuevo/', product_create, name='product_create'),
    path('compras/nueva/', purchase_create, name='purchase_create'),
    path('ventas/nueva/', sale_create, name='sale_create'),
    path('productos/<int:pk>/editar/', product_update, name='product_update'),
    path('productos/<int:pk>/borrar/', product_delete, name='product_delete'),
    path('proveedores/<int:pk>/editar/', supplier_update, name='supplier_update'),
    path('proveedores/<int:pk>/borrar/', supplier_delete, name='supplier_delete'),
    path('movimientos/', movement_history, name='movement_history'),
    path('productos/exportar/csv/', export_products_csv, name='product_export_csv'),
    path('historial/', history, name='history'),


]

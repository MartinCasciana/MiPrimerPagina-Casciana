# Kiosco (Proyecto Django – Patrón MVT)

Proyecto Django para gestionar el stock de un kiosco.  
Incluye:  
- Patrón **MVT** (Models, Views, Templates).  
- **Herencia de HTML** (`base.html`).  
- **4 modelos**: Proveedor, Producto, Compra, Venta.  
- **Formularios** para alta de cada modelo.  
- **Búsqueda** de productos por nombre, código o categoría.  
- **Historial** de compras y ventas con fecha y hora.  
- **CRUD completo**: editar y borrar productos y proveedores.  
- **Paginación** en el listado de productos.  
- **Exportar productos a CSV**.  
- **Validación de stock**: no permite vender más de lo disponible.  

---

## 📦 Requisitos
- Python 3.10+  
- Django 4.2 LTS o 5.x  

---

## ⚙️ Instalación

Clonar el proyecto y entrar en la carpeta:

```bash
git clone https://github.com/tu-usuario/django-kiosco.git
cd django-kiosco
```

Crear y activar un entorno virtual:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Preparar la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```


Correr el servidor:

```bash
python manage.py runserver
```

---

## 🌐 Funcionalidades

### Inicio
- `/` → Página principal con navegación (herencia de `base.html`).

### Proveedores
- `/proveedores/nuevo/` → Alta de proveedor.  
- `/proveedores/<id>/editar/` → Editar proveedor.  
- `/proveedores/<id>/borrar/` → Eliminar proveedor (solo si no tiene productos asociados).

### Productos
- `/productos/nuevo/` → Alta de producto.  
- `/productos/` → Listado de productos con stock calculado.  
  - Incluye **paginación**.  
  - Alerta si stock ≤ 3.  
  - Link para **exportar CSV**.  
- `/productos/<id>/editar/` → Editar producto.  
- `/productos/<id>/borrar/` → Eliminar producto (si no tiene movimientos).

### Compras (entrada de stock)
- `/compras/nueva/` → Registrar compra.  
  - Aumenta el stock del producto.  

### Ventas (salida de stock)
- `/ventas/nueva/` → Registrar venta.  
  - Disminuye el stock del producto.  
  - Valida que no se pueda vender más de lo disponible.  

### Búsqueda
- `/buscar/` → Formulario para buscar productos por **nombre**, **código de barras** o **categoría**.

### Historial
- `/historial/` → Lista unificada de todas las **compras y ventas**.  
  - Muestra producto, cantidad, importe unitario, fecha y hora.  
  - Permite filtrar por nombre de producto.  

---

## 🧪 Orden de prueba sugerido
1. Ingresar a `/` (inicio).  
2. Crear un proveedor en `/proveedores/nuevo/`.  
3. Crear un producto en `/productos/nuevo/` vinculado al proveedor.  
4. Registrar una compra en `/compras/nueva/`.  
   - Verificar en `/productos/` que aumentó el stock.  
5. Registrar una venta en `/ventas/nueva/`.  
   - Verificar en `/productos/` que disminuyó el stock.  
   - Si se intenta vender más de lo disponible, muestra error.  
6. Buscar productos en `/buscar/`.  
7. Ver historial en `/historial/` con compras y ventas ordenadas por fecha.  
8. Editar o borrar productos y proveedores desde la lista.  
9. Probar exportar listado a CSV en `/productos/`.  

---

## 📂 Estructura del proyecto

```
django-kiosco/
│
├─ manage.py
├─ requirements.txt
├─ README.md
│
├─ kiosco_project/
│   ├─ settings.py
│   ├─ urls.py
│   └─ ...
│
└─ app_kiosco/
    ├─ models.py
    ├─ views.py
    ├─ urls.py
    ├─ forms.py
    └─ templates/app_kiosco/
        ├─ base.html
        ├─ home.html
        ├─ search.html
        ├─ product_list.html
        ├─ product_form.html
        ├─ supplier_form.html
        ├─ purchase_form.html
        ├─ sale_form.html
        ├─ history.html
        └─ confirm_delete.html
```

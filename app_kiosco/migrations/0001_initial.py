
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('barcode', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('category', models.CharField(blank=True, max_length=80)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('contact', models.CharField(blank=True, max_length=120)),
                ('phone', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='app_kiosco.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='app_kiosco.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_kiosco.supplier'),
        ),
    ]

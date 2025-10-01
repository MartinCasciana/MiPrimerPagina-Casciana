
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kiosco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Compra'), ('OUT', 'Venta')], max_length=3)),
                ('qty', models.PositiveIntegerField()),
                ('unit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='app_kiosco.product')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'ordering': ['-date'],
            },
        ),
    ]

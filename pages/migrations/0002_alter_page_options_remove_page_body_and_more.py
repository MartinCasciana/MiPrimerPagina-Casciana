
import ckeditor.fields
import django.db.models.deletion

from django.utils import timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={},
        ),
        migrations.RemoveField(
            model_name='page',
            name='body',
        ),
        migrations.RemoveField(
            model_name='page',
            name='created',
        ),
        migrations.RemoveField(
            model_name='page',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='page',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='date_created',
            field=models.DateTimeField(default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pages/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0003_producto_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-13 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_product_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
    ]
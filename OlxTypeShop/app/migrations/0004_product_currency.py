# Generated by Django 4.0.1 on 2022-01-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('1', 'LEI'), ('2', '€')], default=('1', 'LEI'), max_length=5),
        ),
    ]

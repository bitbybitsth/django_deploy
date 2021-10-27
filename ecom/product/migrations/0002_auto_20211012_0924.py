# Generated by Django 3.2.8 on 2021-10-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AddField(
            model_name="product",
            name="delivery",
            field=models.CharField(
                default="India", max_length=40, verbose_name="Delivery Country"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="warranty",
            field=models.IntegerField(default=1, verbose_name="Warranty in Year"),
        ),
    ]

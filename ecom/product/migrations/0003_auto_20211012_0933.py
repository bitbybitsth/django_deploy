# Generated by Django 3.2.8 on 2021-10-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_auto_20211012_0924"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.AddField(
            model_name="product",
            name="pid",
            field=models.IntegerField(
                default=1, primary_key=True, serialize=False, verbose_name="Product ID"
            ),
            preserve_default=False,
        ),
    ]

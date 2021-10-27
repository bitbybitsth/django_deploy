from django.db import models

# Create your models here.


class Product(models.Model):
    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    pid = models.IntegerField(verbose_name="Product ID", primary_key=True)
    name = models.CharField(
        verbose_name="Product's Name", max_length=40, null=False, blank=False
    )
    brand = models.CharField(
        verbose_name="Product's Brand", null=False, blank=False, max_length=40
    )
    price = models.FloatField(verbose_name="Product's Price", null=False, blank=False)
    qty = models.IntegerField(verbose_name="Quantity", default=1)
    warranty = models.IntegerField(verbose_name="Warranty in Year", default=1)
    delivery = models.CharField(
        verbose_name="Delivery Country", max_length=40, default="India"
    )

    def __str__(self):
        return f"{self.name} -> {self.brand}"

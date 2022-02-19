from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class ProductGroup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.TextField()
    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.CASCADE,
        related_name='product',
    )
    product_seller = models.ForeignKey(
        User,
        related_name='product_seller',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='sales_backend/',
        blank=True,
    )
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    discount = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'product_seller','product_group'],
                name='unique_name_product_seller_product_group'
            )
        ]

    def __str__(self):
        return self.name

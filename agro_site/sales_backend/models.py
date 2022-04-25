from django.contrib.auth import get_user_model
from django.db import models
from django.forms import ChoiceField
from users.models import MyUser as User


SCORE = [(i, int(i)) for i in range(1, 6)]

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
    on_sale=models.BooleanField(default=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['name', 'product_seller','product_group'],
    #             name='unique_name_product_seller_product_group'
    #         )
    #     ]

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
        help_text='Комментарий поста',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment',
        verbose_name='Автор',
    )
    text = models.TextField(
        'Комментарий поста',
        help_text='Введите комментарий поста',
    )
    rating = models.DecimalField(
        max_digits=6,
        choices=SCORE,
        decimal_places=0
    )

    def __str__(self):
        return self.text

    def get_avg_rating(self):
        avg_rating = (self.rating) / 5
        return avg_rating
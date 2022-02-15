from rest_framework import serializers

from sales_backend.models import Product, ProductGroup


class ProductSerializer(serializers.ModelSerializer):
    product_group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=ProductGroup.objects.all(),
    )

    class Meta:
        model = Product
        fields = '__all__'

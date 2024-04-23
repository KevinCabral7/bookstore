from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializar

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializar(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    
    class Meta: 
        model = Product
        fields = ['product', 'total']
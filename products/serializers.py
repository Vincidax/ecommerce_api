from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        category = Category.objects.get(id=validated_data.pop("category_id"))
        return Product.objects.create(category=category, **validated_data)

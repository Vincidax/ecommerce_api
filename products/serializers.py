from rest_framework import serializers
from .models import Product, Category

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)  # For creating/updating
    category = CategorySerializer(read_only=True)            # Nested read

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        # Get category safely
        category_id = validated_data.pop("category_id")
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError({"category_id": "Category does not exist."})
        
        # Create product
        return Product.objects.create(category=category, **validated_data)

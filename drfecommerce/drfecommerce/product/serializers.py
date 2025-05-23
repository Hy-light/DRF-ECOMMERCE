from rest_framework import serializers

from .models import Product, Category, Brand, ProductLine, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    
    category_name = serializers.CharField(source="name")
    
    class Meta:
        model = Category
        fields = ["category_name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ["id"]
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ["id", "productline"]


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = [
            "price",
            "sku",
            "stock_qty",
            "order",
            "product_image"
            
        ]


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "slug",
            "brand_name",
            "category_name",
            "product_line"
        ]



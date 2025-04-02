from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db import connection # to inspect queries

from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving all categories.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving all Brand.
    """

    queryset = Brand.objects.all()


    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving  all Product.
    """

    queryset = Product.objects.isactive()  # Use the custom manager to get active products
    
    lookup_field = "slug"
    
    @extend_schema(responses=ProductSerializer)
    def retrieve(self, request, slug="slug"):
        serializer = ProductSerializer(self.queryset.filter(slug=slug).select_related("category", "brand"), many=True,)
        
        data = Response(serializer.data)
        
        return data

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    @action(methods=["get"], detail=False, url_path=r"category/(?P<slug>[\w-]+)",)
    def list_product_by_category_slug(self, request, slug=None):
        """
        List all products in a specific category.
        """

        serializer = ProductSerializer(self.queryset.filter(category__slug=slug), many=True)
        return Response(serializer.data)
    
    
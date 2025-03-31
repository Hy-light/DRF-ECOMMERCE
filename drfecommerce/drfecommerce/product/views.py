from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving all categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving all Brand.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving  all Product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

"""
Factory is used to create dummy database objects needed for testing.
"""

import factory

# from factory import Faker, LazyFunction

from drfecommerce.product.models import Category, Brand, Product, ProductLine, ProductImage


class CategoryFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Category instances.
    """

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Brand instances.
    """

    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Product instances.
    """

    class Meta:
        model = Product

    name = "test_product"
    description = "test_description"
    is_digital = True
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating ProductLine instances.
    """

    class Meta:
        model = ProductLine

    product = factory.SubFactory(ProductFactory)
    sku = "1234"
    stock_qty = 100
    price = 10.00
    is_active = True


class ProductImageFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating ProductImage instances.
    """
    
    class Meta:
        model = ProductImage
    
    alternate_text = "test alternative text"
    url = "test.jpg"
    productline = factory.SubFactory(ProductLineFactory)
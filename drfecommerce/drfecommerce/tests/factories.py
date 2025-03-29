"""
Factory is used to create dummy database objects needed for testing.
"""

import factory
# from factory import Faker, LazyFunction

from drfecommerce.product.models import Category, Brand, Product


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
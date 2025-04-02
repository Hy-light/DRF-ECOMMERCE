import factory
import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategoryModels:
    def test_str_method(self, category_factory):
        """
        Arrange
        Act
        Assert
        """
        # Act
        x = category_factory(name="test_cat")

        # Assert
        assert x.__str__() == "test_cat"


class TestBrandModels:
    def test_str_method(self, brand_factory):
        """
        Arrange
        Act
        Assert
        """
        # Act
        x = brand_factory(name="test_brand")

        # Assert
        assert x.__str__() == "test_brand"


class TestProductModels:
    def test_str_method(self, product_factory):
        """
        Arrange
        Act
        Assert
        """
        # Act
        obj = product_factory(name="test_product")

        # Assert
        assert obj.__str__() == "test_product"


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        # Act
        obj = product_line_factory(sku="12234")

        # Assert
        assert obj.__str__() == "12234"

    def test_clean_method_duplicate_order(self, product_line_factory, product_factory):
        # Arrange
        obj = product_factory()
        product_line_factory(product=obj, order=1)
        with pytest.raises(ValidationError):
            # Act
            product_line_factory(product=obj, order=1).clean()
        
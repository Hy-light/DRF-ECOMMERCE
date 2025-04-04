import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:

    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange
        category_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:

    endpoint = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndpoints:

    endpoint = "/api/product/"

    def test_return_all_product(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
        
    def test_return_single_product_by_slug(self, product_factory, api_client):
        # Arrange
        obj = product_factory(slug="test_product")
        # Act
        response = api_client().get(f"{self.endpoint}{obj.slug}/")
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1
        
    def test_return_products_by_category_slug(self, category_factory, product_factory, api_client):
        # Arrange
        obj = category_factory(slug="test-slug")
        product_factory(category=obj)
        # Act
        response = api_client().get(f"{self.endpoint}category/{obj.slug}/")
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1
        
        



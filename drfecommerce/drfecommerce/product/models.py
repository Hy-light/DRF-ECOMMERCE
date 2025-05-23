from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField
from django.core.exceptions import ValidationError


class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    objects = ActiveQueryset.as_manager()  # Custom manager for active categories

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()  # Custom manager for active products

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    stock_qty = models.IntegerField()
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product", blank=True)
    objects = ActiveQueryset.as_manager()

    def clean(self):
        qs = ProductLine.objects.filter(product=self.product)

        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate order number")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ProductLine, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.sku)


class ProductImage(models.Model):
    alternate_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default="test.jpg") # installed pillow in other to use imagefield
    productline = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name="product_image"
    )
    order = OrderField(unique_for_field="productline", blank=True)
    
    def clean(self):
        qs = ProductImage.objects.filter(productline=self.productline)

        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate order number")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order) 
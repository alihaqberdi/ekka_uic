from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
import string
import random


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Category title'))
    slug = models.SlugField(max_length=255, verbose_name='Category slug',
                            unique=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Size(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sizes')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='colors')
    title = models.CharField(max_length=255)
    color = ColorField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    discount_id = models.ForeignKey("product.Discount", on_delete=models.SET_NULL, related_name='products', null=True,
                                    blank=True)
    text = models.TextField()
    main_image = models.ImageField(null=True)
    status = models.ForeignKey(
        Status, on_delete=models.SET_NULL, null=True
    )
    currency_ids = models.ManyToManyField("product.Currency")

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(6)])
        return slug + random_data

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if Product.objects.filter(slug=self.slug).exists():
            self.slug = self.__generate_slug(self.slug)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    product_price = models.ForeignKey("product.Price", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')


class Price(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='prices')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='prices')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.title + " " + self.size.title + " " + self.color.title


class Discount(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField()
    count = models.PositiveIntegerField(default=100)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.title


class Currency(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

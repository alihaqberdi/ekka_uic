from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import string
import random


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Category title'))
    slug = models.SlugField(max_length=255, verbose_name='Category slug',
                            unique=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField()
    main_image = models.ImageField(null=True)
    count = models.PositiveIntegerField()

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
    image = models.ImageField(upload_to='product_images/')

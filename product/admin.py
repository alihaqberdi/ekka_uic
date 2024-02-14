from django.contrib import admin

# Register your models here.
from product.models import Category, Size, Color, Product, ProductImage, Price, Discount, Currency

admin.site.register([Discount, Currency])


@admin.register(Size)
class AdminSize(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ["id", "title", "slug"]
    list_display_links = ["id", "title", "slug"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    list_display_links = ['id', 'product', 'image']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs


class ColorInline(admin.TabularInline):
    model = Color


class PriceInline(admin.TabularInline):
    model = Price


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class SizeInline(admin.TabularInline):
    model = Size


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', "title", "slug"]
    list_display_links = ['id', "title", "slug"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ColorInline, SizeInline]
    search_fields = ["title"]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', "title"]
    list_display_links = ['id', "title"]
    search_fields = ['title', "category__title", "prices__price"]
    inlines = [PriceInline, ProductImageInline]
    autocomplete_fields = ["category"]
    readonly_fields = ("slug",)


@admin.register(Price)
class AdminPrice(admin.ModelAdmin):
    list_display = ["product", "id", "size", "color", "price", "count"]
    search_fields = ["size__title", "color__title", "product__title"]
    list_display_links = ["product", "id", "size", "color", "price", "count"]
    list_filter = ["size", "color", "price", "count"]
    autocomplete_fields = ["size", "color", "product"]
    inlines = [ProductImageInline]

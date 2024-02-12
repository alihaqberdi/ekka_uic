from product.models import Category, Size, Color, Product, Discount
from modeltranslation.translator import TranslationOptions, translator


class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


class SizeTranslationOptions(TranslationOptions):
    fields = ("title",)


class ColorTranslationOptions(TranslationOptions):
    fields = ("title",)


class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "text")


class DiscountTranslationOptions(TranslationOptions):
    fields = ("title", "text")


translator.register(Category, CategoryTranslationOptions)
translator.register(Size, SizeTranslationOptions)
translator.register(Color, ColorTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Discount, DiscountTranslationOptions)

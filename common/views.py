from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from product.models import Product


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'




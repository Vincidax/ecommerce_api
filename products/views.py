from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
def home(request):
    """
    API Home - directs users to main endpoints
    """
    data = {
        "products": request.build_absolute_uri(reverse('product-list')),
        "categories": request.build_absolute_uri(reverse('category-list')),
        "users": request.build_absolute_uri(reverse('user-list')),
        "message": "Welcome to the E-commerce API! Use these endpoints to explore."
    }
    return Response(data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__title']

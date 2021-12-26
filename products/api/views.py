from django.contrib.auth import get_user_model
from products.api.serializers import ProductSerializer
from products.models import Product
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "slug"


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "slug"

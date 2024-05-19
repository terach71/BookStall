from django.shortcuts import render
from rest_framework import permissions, viewsets
from inventory.models import Book, Author, Complemtry_items, Brand
from inventory.serializers import BookSerializer, AuthorSerializer,\
    ComplentryItemSerializer, BrandSerializer

# Create your views here.

class BookAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny,)

class AuthorAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    permission_classes = (permissions.AllowAny,)

class ComplementryItemAPIView(viewsets.ModelViewSet):
    queryset = Complemtry_items.objects.all().order_by('id')
    serializer_class = ComplentryItemSerializer
    permission_classes = (permissions.AllowAny,)

class BrandAPIView(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer
    permission_classes = (permissions.AllowAny,)

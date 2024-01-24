from rest_framework import serializers
from inventory.models import Book,Author,Complemtry_items,Brand

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('b_type','name','price','pages',
                'desciption','thumbnail',)
        
class AuthorSeralizer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields= '__all__'

class ComplentryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Complemtry_items
        fields = '__all__'
        exclude_fields = ('brand')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields = '__all__'
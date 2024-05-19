from rest_framework import serializers
from inventory.models import Book,Author,Complemtry_items,Brand

class AuthorSerializer(serializers.ModelSerializer):
    """ Author data 
        Fields :
                1. name -> Name of author
                2. age -> Age of author
                3. dob -> Date of birth
                4. media_link ->  Social media links of Author
                5. picture -> Author's Profile pricture
                6. awards -> awards won by Author
    """
    class Meta:
        model=Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Book Data linked with Author data
        Fields :
            1. b_type -> book type
            2. name -> book name
            3. price -> book price
            4. pages -> total number of pages
            5. description -> book description
            6. thumbnail -> pictures of fronts and famous quotes in book
    """
    # author = serializers.ChoiceField(choices=[(i,i.name) for i in Author.objects.all()])
    
    class Meta:
        model=Book
        fields=('b_type','name','price','pages',
                'desciption','thumbnail','author')
        extra_kwargs={'author':{'write_only':True,'required':False}}

        
    
    
class ComplentryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Complemtry_items
        fields = '__all__'
        # exclude_fields = ('brand')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields = '__all__'
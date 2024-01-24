from django.db import models

# Create your models here.

book_types = (('cult','CULTURAL'),('edu','EDUCATIONAL'),('entr','ENTERTAINMENT'))

class Book(models.Model):
    """Book information Book_type, name, author(fg),price, no_of_pages,description,
       thumbnail,highlighted_pics, open_link"""
    b_type = models.CharField(choices=book_types, max_length=50)
    name = models.CharField(max_length=50)
    author = models.ForeignKey("inventory.Author",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    pages = models.IntegerField()
    desciption = models.TextField(max_length=500)
    thumbnail= models.ImageField(upload_to="img/")
    show_pic = models.TextField()


class Author(models.Model):
    """Author information name, age, dob, media_links, profile picture, 
        won_awards
    """
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField( auto_now=False, auto_now_add=False)
    media_links = models.TextField()
    picture = models.FileField( upload_to="img/authors/", max_length=100)
    awards=models.TextField(max_length=500)

class Complemtry_items(models.Model):
    """Complemetry products attribs [typ, material, name,
    price,brand,thumbnail, highlited_pics,description]"""
    i_type = models.CharField( max_length=50)
    material = models.CharField( max_length=50)
    name= models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    brand = models.ForeignKey("inventory.Brand", on_delete=models.CASCADE)
    thumbnail = models.ImageField( upload_to="img/CItems/", height_field=None, width_field=None, max_length=None)
    show_pic = models.TextField()
    description= models.TextField(max_length=500)



class Brand(models.Model):
    """Brand attrbs [name, YOE, description]"""
    name= models.CharField( max_length=50)
    yoe = models.DateField(auto_now=False, auto_now_add=False)
    details= models.TextField( max_length=500)

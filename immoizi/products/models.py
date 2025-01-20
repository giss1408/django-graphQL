from django.db import models
import datetime
from utils.imagesManager.imagesManager_upload import make_thumbnail
from phonenumber_field.modelfields import PhoneNumberField

# Model Category, immo categories like residence, Business, Commerce, Industrie...[ Miete - Kaufen ]
#!!! Create enum for residence category
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# Model Tenant, nom et prenoms, ID, nbr de maisons, status payment, expire date. 
class Tenant(models.Model): # grocery
    nomPrenoms = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    quantity = models.IntegerField()# nbr de maisons
    status_payment = models.BooleanField(default=False)
    expire_date = models.DateField(default=datetime.date.today)
    date_created = models.DateField(auto_now_add=True)
    phone_number = PhoneNumberField( blank=True )


    class Meta:
        ordering = [ '-date_created' ]

    def __str__(self):
        return self.nomPrenoms


#class Gui(models.Model):
#    api_version = models.IntegerField(default=00)
#    images = models.ArrayField( models.URLField(max_length=200), size=10)

# Model Descrition prix, surface, nbr de chambres
class Description(models.Model):# book
    title = models.CharField(max_length=150) # description du proprietaire
    country = models.CharField(max_length=100, default="Côte d'Ivoire") # pays
    city = models.CharField(max_length=100, default='Abidjan') # ville
    district = models.CharField(max_length=100, default='Marcory') # quartier
    tenant = models.CharField(max_length=100, default='Anonyme') # Nom du proprietaire ou agence
    isbn = models.CharField(max_length=13) # numero d'inscription du tenant
    rooms = models.IntegerField() # nbr de pieces
    surface_m2 = models.IntegerField(default=00)
    price = models.IntegerField() # prix mensuel/ rent
    description = models.TextField() #description detaillee du proprietaire
    status = models.BooleanField() # oqp / libre
    date_created = models.DateField(auto_now_add=True)
    date_toEnter = models.DateField(default=datetime.date.today) # Libre a partir de 
    category = models.ForeignKey(Category, related_name='description', on_delete=models.CASCADE)
    imageurl = models.URLField()# Shoud be an array of links for this element - Create class GUI
    #nombre de photos
    product_tag = models.CharField(max_length=10)
    bailleur = models.ForeignKey(Tenant, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = [ '-date_created' ]

    def __str__(self):
        return self.title
    
# models.py Test upload images
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    #thumbnail = models.ImageField(upload_to='images/')
 
    '''
    def save(self, *args, **kwargs):
        self.thumbnail = make_thumbnail(self.hotel_Main_Img, size=(100, 100))
        
        super().save(*args, **kwargs)
        '''

'''
# import the `make_thumbnail` function
from some_file import make_thumbnail

class MyModel(models.Model):
    image = models.ImageField()
    thumbnail = models.ImageField()

    def save(self, *args, **kwargs):
        self.thumbnail = make_thumbnail(self.image, size=(100, 100))

        super().save(*args, **kwargs)
'''
from django.db import models
import datetime

# Model Category, immo categories like residence, Business, Commerce, Industrie...[ Miete - Kaufen ]
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# Model Descrition prix, surface, nbr de chambres
class Description(models.Model):
    title = models.CharField(max_length=150) # description du proprietaire
    tenant = models.CharField(max_length=100, default='Anonyme') # Nom du proprietaire ou agence
    isbn = models.CharField(max_length=13) # numero d'inscription du tenant
    pieces = models.IntegerField() # nbr de pieces
    price = models.IntegerField() # prix mensuel
    description = models.TextField() #description detaillee du proprietaire
    status = models.BooleanField() # oqp / libre
    date_created = models.DateField(auto_now_add=True)
    date_toEnter = models.DateField(default=datetime.date.today) # Libre a partir de 
    category = models.ForeignKey(Category, related_name='description', on_delete=models.CASCADE)
    imageurl = models.URLField()
    product_tag = models.CharField(max_length=10)


    class Meta:
        ordering = [ '-date_created' ]

    def __str__(self):
        return self.title

class Tenant(models.Model):
    nomPrenoms = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    quantity = models.IntegerField()# nbr de maisons
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = [ '-date_created' ]

    def __str__(self):
        return self.nomPrenoms

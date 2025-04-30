from django.db import models
from datetime import datetime

# compagnie - owner of the real estate
class Landlord(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profiles', default='logo.png')
    phone = models.CharField(max_length=11, default='')
    bio = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='Abidjan')
    location = models.CharField(max_length=40, default='')
    creationDate = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=False)
    score = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.name}'

# Person or compagnie - rent a property
class Tenant(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, default='')
    bio = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='Abidjan')
    location = models.CharField(max_length=40, default='')
    creationDate = models.DateTimeField(default=datetime.now)
    score = models.IntegerField(default=5)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class AfricanLocation(models.Model):
    city = models.CharField(max_length=100, default='ABIDJAN')
    suburb = models.CharField(max_length=100, default='MARCORY')
    situation=models.CharField(max_length=100, default='Quartier-Maroc')
    description=models.CharField(max_length=200)# Some description to locate the position when no adress exist

    def __str__(self):
        return f"{self.city} - {self.suburb} - {self.situation}"
    
# Objects
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('APARTMENT', 'Apartment'),
        ('HOUSE', 'House'),
        ('STUDIO', 'Studio'),
        ('COMMERCIAL', 'Commercial'),
        ('TERRAIN', 'Terrain'),
    ]

    RENT_SALE_CHOICES = [
        ('SALE', 'Sale'),
        ('RENT', 'Rent')
    ]
    ourCustomer= models.ForeignKey(Landlord, on_delete=models.CASCADE)
    mieter = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    africanLocation=models.ForeignKey(AfricanLocation, on_delete=models.CASCADE)# In w-africa, places are found with city-suburb-subsuburb and more descriptions
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='', blank=True)
    address = models.CharField(max_length=200)
    estate_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='House')
    rent_sale = models.CharField(max_length=20, choices=RENT_SALE_CHOICES, default='Sale')
    price = models.IntegerField()
    kitchen = models.IntegerField()
    hall = models.CharField(max_length=3)
    balcony = models.CharField(max_length=3)
    desc = models.CharField(max_length=200)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    is_available = models.BooleanField(default=True)
    standing=models.IntegerField(default=5)
    #sold = models.BooleanField(default=False)
    #sold_time = models.DateTimeField(default=datetime.now, blank=True)
   # photo_main = models.ImageField(upload_to='listings_main')
    #photo_1 = models.ImageField(upload_to='listings_1', blank=True)
    #photo_2 = models.ImageField(upload_to='listings_1', blank=True)
    #photo_3 = models.ImageField(upload_to='listings_1', blank=True)
    #photo_4 = models.ImageField(upload_to='listings_1', blank=True)
    #photo_5 = models.ImageField(upload_to='listings_1', blank=True)
    #photo_6 = models.ImageField(upload_to='listings_1', blank=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    #unless = models.CharField(default='', max_length=20)

    # 🔥 Used for previews and main image
    #main_image = models.ImageField(upload_to='property_images/main/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.standing}"

# Lease Model
class Lease(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    ourCustomer = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)
    score = models.IntegerField(default=5)

    def __str__(self):
        return f"Lease for {self.property} - {self.tenant}"

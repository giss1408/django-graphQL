import graphene
from graphene_django import DjangoObjectType
from .models import Landlord, Property, Tenant, Lease, AfricanLocation
from datetime import datetime

''' AfricanLocationType'''
class AfricanLocationType(DjangoObjectType):
    class Meta:
        model= AfricanLocation
        fields = ('id', 'city', 'suburb', 'situation', 'description')

class AfricanLocationInput(graphene.InputObjectType):
    city = graphene.String(max_length=11, default='')
    suburb = graphene.String(max_length=11, default='')
    situation = graphene.String(max_length=11, default='')
    description = graphene.String(max_length=100, default='')

class UpdateAfricanLocation(graphene.Mutation):
    class Arguments:
        # Mutation to update african location
        input = AfricanLocationInput( required=True )
        id = graphene.ID()

    africanLocation = graphene.Field(AfricanLocationType)

    @classmethod
    def mutate( cls, root, info, input, id):
        africanLocation = AfricanLocation.objects.get(pk=id)
        africanLocation.city = input.city
        africanLocation.suburb = input.suburb
        africanLocation.situation = input.situation
        africanLocation.description = input.description

        africanLocation.save()

        return UpdateLandlord(africanLocation=africanLocation)

class CreateAfricanLocation(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        input = AfricanLocationInput(required=True)

    # Class attributes define the response of the mutation
    africanLocation = graphene.Field(AfricanLocationType)

    @classmethod
    def mutate(cls, root, info, input, id):
        africanLocation = AfricanLocation()
        africanLocation.city = input.city
        africanLocation.suburb = input.suburb
        africanLocation.situation = input.situation
        africanLocation.description = input.description
        africanLocation.save()

        return CreateLandlord(africanLocation=africanLocation)

''' LandlordType'''
class LandlordType(DjangoObjectType):
    class Meta:
        model = Landlord
        fields = ('id', 'name', 'bio', 'phone', 'city', 'location', 'active','score')

class LandlordInput(graphene.InputObjectType):
    name = graphene.String()
    #image = graphene.Field(ImageField)
    phone = graphene.String(max_length=11, default='')
    bio = graphene.String(max_length=100, default='')
    city = graphene.String(max_length=20, default='Abidjan')
    location = graphene.String(max_length=40, default='Zone 4')
    active = graphene.Boolean(default=False)
    score = graphene.Decimal(decimal_places=2, max_digits=2)

class UpdateLandlord(graphene.Mutation):
    class Arguments:
        # Mutation to update category
        input = LandlordInput( required=True )
        id = graphene.ID()

    landlord = graphene.Field(LandlordType)

    @classmethod
    def mutate( cls, root, info, input, id):
        landlord = Landlord.objects.get(pk=id)
        landlord.name = input.name
        landlord.phone = input.phone
        landlord.bio = input.bio
        landlord.city = input.city
        landlord.location = input.location
        landlord.active = input.active
        landlord.score = input.score

        landlord.save()

        return UpdateLandlord(landlord=landlord)

class CreateLandlord(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        input = LandlordInput(required=True)

    # Class attributes define the response of the mutation
    landlord = graphene.Field(LandlordType)

    @classmethod
    def mutate(cls, root, info, input, id):
        landlord = Landlord()
        landlord.name = input.name
        landlord.phone = input.phone
        landlord.bio = input.bio
        landlord.city = input.city
        landlord.location = input.location
        landlord.active = input.active
        landlord.score = input.score
        landlord.save()

        return CreateLandlord(landlord=landlord)

''' TenantType'''
class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant
        fields = ('id', 'name', 'bio', 'phone', 'city', 'location', 'active', 'score')

class TenantInput(graphene.InputObjectType):
    name = graphene.String( required=True)
    phone = graphene.String(max_length=11, default='')
    bio = graphene.String(max_length=100, default='')
    city = graphene.String(max_length=20, default='marcory')
    location = graphene.String(max_length=40, default='')
    date = graphene.String(max_length=40, default='')
    active = graphene.Boolean(default=False)
    score = graphene.Int(default=5)

class CreateTenant(graphene.Mutation):
    class Arguments:
        input = TenantInput(required=True)

    tenant = graphene.Field(TenantType)

    @classmethod
    def mutate(cls, root, info, input):
        tenant = Tenant()
        tenant.name = input.title
        tenant.bio = input.bio
        tenant.city = input.city
        tenant.phone = input.phone
        tenant.location = input.location
        tenant.creationDate = input.creationDate
        tenant.active = input.active
        tenant.score = input.score
        tenant.save()

        return CreateTenant(tenant=tenant)

class UpdateTenant(graphene.Mutation):
    class Arguments:
        input = TenantInput(required=True)
        id = graphene.ID()

    tenant = graphene.Field(TenantType)

    @classmethod
    def mutate(cls, root, info, input, id):
        tenant = Tenant.objects.get(pk=id)
        tenant.name = input.title
        tenant.bio = input.bio
        tenant.city = input.city
        tenant.phone = input.phone
        tenant.location = input.location
        tenant.creationDate = input.creationDate
        tenant.active = input.active
        tenant.score = input.score
        tenant.save()

        return UpdateTenant(tenant=tenant)  

''' PropertyType'''
class PropertyType(DjangoObjectType):
    class Meta:
        model = Property
        fields = ('id', 'ourCustomer', 'mieter', 'title', 'address', 'estate_type', 'rent_sale', 'price', 'kitchen', 'hall', 'balcony', 'desc', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'is_available', 'is_published', 'standing')

class PropertyInput(graphene.InputObjectType):
    PROPERTY_TYPE_CHOICES = [
        ('APARTMENT', 'Apartment'),
        ('HOUSE', 'House'),
        ('STUDIO', 'Studio'),
        ('COMMERCIAL', 'Commercial'),
    ]

    CITY_CHOICES = [
        ('ABIDJAN', 'Abidjan'),
        ('BOUAKE', 'Bouake')
    ]

    RENT_SALE_CHOICES = [
        ('SALE', 'Sale'),
        ('RENT', 'Rent')
    ]
    title = graphene.String(max_length=200)
   # slug = models.SlugField(unique=True, default='', blank=True)
    address = graphene.String(max_length=200)
    price = graphene.Int()
    kitchen = graphene.Int(default=1)
    hall = graphene.String(max_length=3)
    balcony = graphene.String(max_length=3)
    desc = graphene.String(max_length=200)
    bedrooms = graphene.Int(default=0)
    bathrooms = graphene.Int(default=1)
    garage = graphene.Int(default=0)
    sqft = graphene.Int()
    is_available = graphene.Boolean(default=True)
    is_published = graphene.Boolean(default=False)
    standing=graphene.Int(default=0)

class CreateProperty(graphene.Mutation):
    class Arguments:
        input = PropertyInput(required=True)

    property = graphene.Field(PropertyType)

    @classmethod
    def mutate(cls, root, info, input):
        property = Property()
        property.ourCustomer = input.ourCustomer
        property.mieter = input.mieter
        property.city = input.city
        property.title = input.title
        property.address = input.address
        property.city = input.city
        property.estate_type = input.estate_type
        property.rent_sale = input.rent_sale
        property.price = input.price
        property.kitchen = input.kitchen
        property.hall = input.hall
        property.balcony = input.balcony
        property.desc = input.desc
        property.bedrooms = input.bedrooms
        property.bathrooms = input.bathrooms
        property.garage = input.garage
        property.sqft = input.sqft
        property.is_available = input.is_available
        property.is_published = input.is_published
        property.standing=input.standing
        #property.published_date = input.published_date

        property.save()

        return CreateProperty(property=property)

class UpdateProperty(graphene.Mutation):
    class Arguments:
        input = PropertyInput(required=True)
        id = graphene.ID()

    property = graphene.Field(PropertyType)

    @classmethod
    def mutate(cls, root, info, input, id):
        property = Property.objects.get(pk=id)
        property.ourCustomer = input.ourCustomer
        property.mieter = input.mieter
        property.city = input.city
        property.title = input.title
        property.address = input.address
        property.city = input.city
        property.estate_type = input.estate_type
        property.rent_sale = input.rent_sale
        property.price = input.price
        property.kitchen = input.kitchen
        property.hall = input.hall
        property.balcony = input.balcony
        property.desc = input.desc
        property.bedrooms = input.bedrooms
        property.bathrooms = input.bathrooms
        property.garage = input.garage
        property.sqft = input.sqft
        property.is_available = input.is_available
        property.is_published = input.is_published
        property.standing=input.standing
       # property.published_date = input.published_date

        property.save()

        return UpdateTenant(property=property)

''' LeaseType'''
class LeaseType(DjangoObjectType):
    class Meta:
        model = Lease
        fields = ('id', 'property', 'tenant', 'ourCustomer', 'monthly_rent', 'security_deposit',  'is_active', 'score')

class LeaseInput(graphene.InputObjectType):
   # property = graphene.Field(PropertyType) Input field cab not be resolved
    #tenant = graphene.Field(TenantType) Input field cab not be resolved
    #ourCustomer = graphene.Field(LandlordType) Input field cab not be resolved
   # start_date = graphene.DateField()
    #end_date = graphene.DateField(null=True, blank=True)
    monthly_rent = graphene.Decimal(max_digits=10, decimal_places=2)
    security_deposit = graphene.Decimal(max_digits=10, decimal_places=2)
    is_active = graphene.Boolean(default=False)
    score = graphene.Int(default=5)

class CreateLease(graphene.Mutation):
    class Arguments:
        input = LeaseInput(required=True)

    lease = graphene.Field(LeaseType)

    @classmethod
    def mutate(cls, root, info, input):
        lease = Lease()
        lease.property = input.property
        lease.tenant = input.tenant
        lease.ourCustomer = input.ourCustomer
        #lease.start_date = input.start_date
        #lease.end_date = input.end_date
        lease.monthly_rent = input.monthly_rent
        lease.security_deposit = input.security_deposit
        lease.score = input.score
        lease.is_active = input.is_active
        lease.save()

        return CreateLease(lease=lease)

class UpdateLease(graphene.Mutation):
    class Arguments:
        input = LeaseInput(required=True)
        id = graphene.ID()

    lease = graphene.Field(LeaseType)

    @classmethod
    def mutate(cls, root, info, input, id):
        lease = Lease.objects.get(pk=id)
        lease.property = input.property
        lease.tenant = input.tenant
        lease.ourCustomer = input.ourCustomer
        #lease.start_date = input.start_date
        #lease.end_date = input.end_date
        lease.monthly_rent = input.monthly_rent
        lease.security_deposit = input.security_deposit
        #lease.score = input.score
        lease.is_active = input.is_active
        lease.save()

        return UpdateLease(lease=lease)

class Query(graphene.ObjectType):
    landlords = graphene.List(LandlordType)
    leases = graphene.List(LeaseType)
    tenants = graphene.List(TenantType)
    properties = graphene.List(PropertyType)
    africanLocations = graphene.List(AfricanLocationType)

    def resolve_landlords( root, info, **kwargs):
        return Landlord.objects.all()

    def resolve_leases( root, info, **kwargs):
        return Lease.objects.all()

    def resolve_properties( root, info, **kwargs):
        return Property.objects.all()

    def resolve_tenants( root, info, **kwargs):
        return Tenant.objects.all()

    def resolve_africanLocations( root, info, **kwargs):
        return AfricanLocation.objects.all()

class Mutation(graphene.ObjectType):
    update_landlord = UpdateLandlord.Field()
    create_landlord = CreateLandlord.Field()

    create_teant = CreateTenant.Field()
    update_tenant = UpdateTenant.Field()

    create_property = CreateProperty.Field()
    update_property = UpdateProperty.Field()

    create_lease = CreateLease.Field()
    update_lease = UpdateLease.Field()

    create_africanLocation = CreateAfricanLocation.Field()
    update_africanLocation = UpdateAfricanLocation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

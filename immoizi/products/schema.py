import graphene
from graphene_django import DjangoObjectType
from .models import Category, Description, Tenant

# Category Type
class CategoryType(DjangoObjectType):
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
        id = graphene.ID(required=True)
        title = graphene.String(required=True)

    landlord = graphene.Field(LandlordType)

    @classmethod
    def mutate(cls, root, info, id, title):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        return UpdateCategory(category=category)

class CreateLandlord(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category.objects.create(title=title)
        return CreateCategory(category=category)

# Description Type
class DescriptionType(DjangoObjectType):
    class Meta:
        model = Description
        fields = (
            'id', 'title', 'tenant', 'country', 'city', 'district', 'isbn',
            'rooms', 'price', 'description', 'status', 'date_created',
            'date_toEnter', 'category', 'imageurl', 'product_tag', 'bailleur', 'thumbnail', 'image_1', 'image_2', 'image_3', 'image_4', 'main_image',
            'surface_m2',
        )

class DescriptionInput(graphene.InputObjectType):
    title = graphene.String()
    country = graphene.String()
    city = graphene.String()
    district = graphene.String()
    bailleur = graphene.String()
    status = graphene.String()
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
        description = Description.objects.create(
            title=input.title,
            country=input.country,
            city=input.city,
            district=input.district,
            bailleur=input.bailleur,
            status=input.status,
            price=input.price,
        )
        return CreateDescription(description=description)

class UpdateProperty(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = DescriptionInput(required=True)

    property = graphene.Field(PropertyType)

    @classmethod
    def mutate(cls, root, info, id, input):
        description = Description.objects.get(pk=id)
        for field in ['title', 'bailleur', 'country', 'city', 'district', 'status', 'price']:
            setattr(description, field, getattr(input, field, getattr(description, field)))
        description.save()
        return UpdateDescription(description=description)

# Tenant Type
class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant
        fields = (
            'id', 'nomPrenoms', 'isbn', 'quantity',
            'date_created', 'status_payment', 'expire_date',
        )

class Query(graphene.ObjectType):
    landlords = graphene.List(LandlordType)
    leases = graphene.List(LeaseType)
    tenants = graphene.List(TenantType)
    properties = graphene.List(PropertyType)
    africanLocations = graphene.List(AfricanLocationType)

    def resolve_landlords( root, info, **kwargs):
        return Landlord.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_descriptions(self, info, **kwargs):
        return Description.objects.all()

    def resolve_tenants(self, info, **kwargs):
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

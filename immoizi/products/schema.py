import graphene
from graphene_django import DjangoObjectType
from .models import Category, Description, Tenant

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')

class DescriptionType(DjangoObjectType):
    class Meta:
        model = Description
        fields = (
            'id',
            'title',
            'tenant',
            'country',
            'city',
            'district',
            'isbn',
            'rooms',
            'price',
            'description',
            'status',
            'date_created',
            'date_toEnter',
            'category',
            'imageurl',
            'product_tag',
            'bailleur',
            'surface_m2',
        )

class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant
        fiels = (
            'id',
            'nomPrenoms',
            'isbn',
            'quantity',
            'date_created',
            'status_payment',
            'expire_date',
        )

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    descriptions = graphene.List(DescriptionType)
    tenants = graphene.List(TenantType)

    def resolve_categories( root, info, **kwargs):
        return Category.objects.all()

    def resolve_descriptions( root, info, **kwargs):
        return Description.objects.all()

    def resolve_tenants( root, info, **kwargs):
        return Tenant.objects.all()

schema = graphene.Schema(query=Query)